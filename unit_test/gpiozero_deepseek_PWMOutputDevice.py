from gpiozero import DigitalOutputDevice, PWMOutputDevice
import time

# 引脚定义
DIR = 20
STEP = 21
CW = True     # 顺时针方向
CCW = False   # 逆时针方向
SPR = 1600    # 每转步数 (Steps Per Revolution)

class StepperMotor:
    def __init__(self, dir_pin=DIR, step_pin=STEP, spr=SPR):
        """
        初始化步进电机控制器
        :param dir_pin: 方向控制引脚 (BCM编号)
        :param step_pin: 步进脉冲引脚 (BCM编号)
        :param spr: 每转步数
        """
        self.dir_pin = DigitalOutputDevice(dir_pin)
        # 使用 initial_value 替代 duty_cycle
        self.step_pin = PWMOutputDevice(step_pin, frequency=1, initial_value=0.5)
        self.spr = spr
        self.current_position = 0  # 当前位置（步数）
        self.is_moving = False     # 电机移动状态
        self.current_direction = CW  # 当前方向
        
        # 初始状态设置
        self.set_direction(CW)
        self.stop()
        print(f"步进电机已初始化 | DIR:BCM{dir_pin}, STEP:BCM{step_pin}, SPR:{spr}")
    
    def set_direction(self, direction):
        """设置电机转动方向"""
        self.dir_pin.value = 1 if direction == CW else 0
        self.current_direction = direction
        print(f"方向设置为: {'顺时针(CW)' if direction == CW else '逆时针(CCW)'}")
    
    def rotate(self, rpm, duration):
        """
        以指定转速持续转动一段时间
        :param rpm: 转速 (转/分钟)
        :param duration: 持续时间 (秒)
        """
        if rpm <= 0:
            print("错误：转速必须大于0")
            return
            
        # 计算所需频率 (Hz)
        frequency = (rpm * self.spr) / 60.0
        
        print(f"开始旋转 | RPM: {rpm}, 持续时间: {duration:.2f}秒")
        self.is_moving = True
        self.step_pin.frequency = frequency
        time.sleep(duration)
        self.stop()
    
    def move_steps(self, steps, rpm=30):
        """
        移动指定步数
        :param steps: 移动步数 (正数)
        :param rpm: 转速 (转/分钟)
        """
        if steps <= 0:
            print("错误：步数必须大于0")
            return
            
        # 计算所需时间和频率
        duration = abs(steps) / (self.spr * rpm / 60.0)
        frequency = (rpm * self.spr) / 60.0
        
        print(f"移动 {steps} 步 | RPM: {rpm}, 预计时间: {duration:.2f}秒")
        self.is_moving = True
        self.step_pin.frequency = frequency
        time.sleep(duration)
        
        # 更新位置
        direction_factor = 1 if self.current_direction == CW else -1
        self.current_position += steps * direction_factor
        self.stop()
    
    def move_degrees(self, degrees, rpm=30):
        """
        旋转指定角度
        :param degrees: 旋转角度 (正数)
        :param rpm: 转速 (转/分钟)
        """
        steps = int((degrees / 360.0) * self.spr)
        print(f"旋转 {degrees}° ≈ {steps} 步")
        self.move_steps(steps, rpm)
    
    def move_revolutions(self, revolutions, rpm=30):
        """
        旋转指定圈数
        :param revolutions: 旋转圈数
        :param rpm: 转速 (转/分钟)
        """
        steps = int(revolutions * self.spr)
        print(f"旋转 {revolutions} 圈 = {steps} 步")
        self.move_steps(steps, rpm)
    
    def set_position(self, position):
        """设置当前位置（步数）"""
        self.current_position = position
        print(f"当前位置设置为: {position} 步")
    
    def get_position(self):
        """获取当前位置（步数）"""
        return self.current_position
    
    def stop(self):
        """停止电机"""
        self.step_pin.frequency = 0
        self.is_moving = False
        print("电机已停止")
    
    def release(self):
        """释放资源"""
        self.stop()
        self.dir_pin.close()
        self.step_pin.close()
        print("资源已释放")

# ==================== 测试代码 ==================== 
if __name__ == "__main__":
    # 创建步进电机对象
    motor = StepperMotor(dir_pin=DIR, step_pin=STEP, spr=SPR)
    
    try:
        # 测试1：顺时针旋转180度（10 RPM）
        print("\n=== 测试1: 旋转180度 ===")
        motor.set_direction(CW)
        motor.move_degrees(180, rpm=10)
        
        # 测试2：逆时针旋转1圈（30 RPM）
        print("\n=== 测试2: 逆时针旋转1圈 ===")
        motor.set_direction(CCW)
        motor.move_revolutions(1, rpm=30)
        
        # 测试3：精确移动1600步（20 RPM）
        print("\n=== 测试3: 精确移动1600步 ===")
        motor.move_steps(1600, rpm=20)
        
        # 测试4：连续旋转5秒（15 RPM）
        print("\n=== 测试4: 连续旋转5秒 ===")
        motor.set_direction(CW)
        motor.rotate(rpm=15, duration=5)
        
        # 显示最终位置
        print(f"\n最终位置: {motor.get_position()} 步")
    
    except KeyboardInterrupt:
        print("程序被用户中断")
    
    finally:
        motor.release()