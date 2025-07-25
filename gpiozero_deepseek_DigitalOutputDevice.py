from time import sleep
from gpiozero import DigitalOutputDevice
import sys

# 引脚定义
DIR = 20
STEP = 21
CW = True   # 顺时针方向
CCW = False # 逆时针方向
SPR = 1600  # 每转步数

class StepperMotor:
    def __init__(self, dir_pin=DIR, step_pin=STEP, spr=SPR):
        """
        初始化步进电机控制器
        :param dir_pin: 方向控制引脚 (BCM编号)
        :param step_pin: 步进脉冲引脚 (BCM编号)
        :param spr: 每转步数
        """
        self.dir_pin = DigitalOutputDevice(dir_pin)
        self.step_pin = DigitalOutputDevice(step_pin)
        self.spr = spr
        self.current_position = 0  # 当前位置（步数）
        self.current_direction = CW  # 当前方向
        
        # 初始状态设置
        self.set_direction(CW)
        print(f"步进电机已初始化 | DIR:BCM{dir_pin}, STEP:BCM{step_pin}, SPR:{spr}")
    
    def set_direction(self, direction):
        """设置电机转动方向"""
        self.dir_pin.value = direction
        self.current_direction = direction
        direction_name = "顺时针(CW)" if direction == CW else "逆时针(CCW)"
        print(f"方向设置为: {direction_name}")
        return self
    
    def step(self, delay=0.001):
        """发送一个步进脉冲"""
        self.step_pin.on()
        sleep(delay)
        self.step_pin.off()
        sleep(delay)
        
        # 更新位置
        direction_factor = 1 if self.current_direction == CW else -1
        self.current_position += direction_factor
    
    def move_steps(self, steps, delay=0.001):
        """
        移动指定步数
        :param steps: 移动步数 (正数)
        :param delay: 步进延迟 (秒)，控制速度
        """
        if steps <= 0:
            print("错误：步数必须大于0")
            return
            
        print(f"移动 {steps} 步 | 延迟: {delay*1000:.3f}ms")
        
        for i in range(steps):
            self.step(delay)
            # 显示进度
            if i % 100 == 0 or i == steps - 1:
                progress = (i + 1) / steps * 100
                sys.stdout.write(f"\r进度: {progress:.1f}% [{'='*int(progress/2)}{' '*(50-int(progress/2))}]")
                sys.stdout.flush()
        
        print()  # 换行
        return self
    
    def move_degrees(self, degrees, delay=0.001):
        """
        旋转指定角度
        :param degrees: 旋转角度
        :param delay: 步进延迟 (秒)
        """
        steps = int((abs(degrees) / 360.0) * self.spr)
        direction = CW if degrees >= 0 else CCW
        
        print(f"旋转 {degrees}° ≈ {steps} 步")
        self.set_direction(direction).move_steps(steps, delay)
        return self
    
    def move_revolutions(self, revolutions, delay=0.001):
        """
        旋转指定圈数
        :param revolutions: 旋转圈数
        :param delay: 步进延迟 (秒)
        """
        steps = int(abs(revolutions) * self.spr)
        direction = CW if revolutions >= 0 else CCW
        
        print(f"旋转 {revolutions} 圈 = {steps} 步")
        self.set_direction(direction).move_steps(steps, delay)
        return self
    
    def set_position(self, position):
        """设置当前位置（步数）"""
        self.current_position = position
        print(f"当前位置设置为: {position} 步")
        return self
    
    def get_position(self):
        """获取当前位置（步数）"""
        return self.current_position
    
    def release(self):
        """释放资源"""
        self.dir_pin.close()
        self.step_pin.close()
        print("资源已释放")

# ==================== 测试代码 ==================== 
if __name__ == "__main__":
    # 创建步进电机对象
    motor = StepperMotor(dir_pin=DIR, step_pin=STEP, spr=SPR)
    
    try:
        # 测试1：顺时针旋转180度（中等速度）
        print("\n=== 测试1: 顺时针旋转180度 ===")
        motor.move_degrees(180, delay=0.001)
        
        # 测试2：逆时针旋转1圈（快速）
        print("\n=== 测试2: 逆时针旋转1圈 ===")
        motor.move_revolutions(-1, delay=0.0005)
        
        # # 测试3：精确移动3200步（慢速）
        # print("\n=== 测试3: 精确移动3200步 ===")
        # motor.move_steps(3200, delay=0.002)
        
        # # 测试4：加速旋转
        # print("\n=== 测试4: 加速旋转 ===")
        # motor.set_direction(CW)
        # motor.move_steps(SPR, 0.001)     # 初始速度
        # motor.move_steps(SPR*2, 0.0005)  # 加速
        # motor.move_steps(SPR*3, 0.0001)  # 高速
        
        # 显示最终位置
        print(f"\n最终位置: {motor.get_position()} 步")
    
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    
    finally:
        motor.release()