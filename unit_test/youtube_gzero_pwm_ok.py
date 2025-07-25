# Note: Ensure TB6600 switches are set correctly (2,5 and 6 ON for 2.5A max at 12V)
# conda activate gzero_env
# python youtube_gzero_pwm.py
from time import sleep
from gpiozero import DigitalOutputDevice, PWMOutputDevice
import math

# 引脚定义
DIR = 20
STEP = 21
CW = True
CCW = False
SPR = 1600  # 每转步数

# 创建方向控制对象
dir_pin = DigitalOutputDevice(DIR)

# 使用硬件PWM控制步进脉冲
step_pin = PWMOutputDevice(STEP, frequency=1000, initial_value=0)

# 设置旋转方向
dir_pin.value = CW

# 优化后的步进函数 - 使用硬件PWM
def smooth_step_motor(steps, target_delay, acceleration=0.00005):
    """
    带加速/减速控制的步进函数
    :param steps: 步数
    :param target_delay: 目标脉冲间隔(秒)
    :param acceleration: 加速度(秒/步)
    """
    if target_delay <= 0:
        print(f"无效的延时参数: {target_delay}，跳过此步骤")
        return
    
    # 计算目标频率 (Hz)
    target_freq = 1 / (2 * target_delay)  # 一个完整脉冲周期 = 2 * 延时
    
    # 频率限制 (根据驱动器能力调整)
    max_freq = 50000  # TB6600最大支持100kHz，但实际中保守使用50kHz
    if target_freq > max_freq:
        print(f"警告: 频率 {target_freq:.1f}Hz 超过安全上限 {max_freq}Hz，限制为上限值")
        target_freq = max_freq
    
    # 设置初始频率（低于目标频率）
    start_freq = min(1000, target_freq)  # 从1kHz开始
    step_pin.frequency = start_freq
    step_pin.value = 0.5  # 50%占空比启动
    
    # 初始化加速阶段变量
    steps_accel = 0
    steps_decel = 0
    
    # 加速阶段（如果目标频率高于初始频率）
    if acceleration > 0 and target_freq > start_freq:
        # 计算加速所需步数
        steps_accel = min(steps // 3, int((target_freq - start_freq) / acceleration))
        print(f"加速阶段: {steps_accel}步, {start_freq:.1f}Hz -> {target_freq:.1f}Hz")
        
        # 执行加速
        for i in range(steps_accel):
            current_freq = start_freq + (i * acceleration)
            if current_freq > target_freq:
                current_freq = target_freq
            step_pin.frequency = current_freq
            sleep(2 / current_freq)  # 等待一个完整脉冲周期
    
    # 恒速阶段
    step_pin.frequency = target_freq
    steps_constant = max(0, steps - steps_accel - steps_decel)  # 确保非负
    
    if steps_constant > 0:
        sleep_time = steps_constant * (1 / target_freq)
        print(f"恒速阶段: {steps_constant}步, {target_freq:.1f}Hz, 运行时间: {sleep_time:.3f}秒")
        sleep(sleep_time)
    
    # 减速阶段（如果有加速阶段）
    if acceleration > 0 and target_freq > start_freq and steps_accel > 0:
        steps_decel = steps_accel  # 减速步数与加速相同
        print(f"减速阶段: {steps_decel}步, {target_freq:.1f}Hz -> {start_freq:.1f}Hz")
        
        # 执行减速
        for i in range(steps_decel, 0, -1):
            current_freq = start_freq + (i * acceleration)
            if current_freq > target_freq:
                current_freq = target_freq
            step_pin.frequency = current_freq
            sleep(2 / current_freq)  # 等待一个完整脉冲周期
    
    # 停止PWM
    step_pin.value = 0
    print(f"完成 {steps} 步运动")

# 主程序
try:
    print("启动电机控制...")
    

    # 测试不同速度 - 带加速/减速控制
    smooth_step_motor(SPR, 0.001)      # 低速启动 (500Hz)
    smooth_step_motor(SPR, 0.0001)     # 中等速度 (5kHz)
    smooth_step_motor(SPR, 0.00008)    # 较高速度 (6.25kHz)
    smooth_step_motor(SPR, 0.00007)  # 降速运行 (7.14kHz)
    smooth_step_motor(SPR, 0.0001)     # 中等速度 (5kHz)
    smooth_step_motor(SPR, 0.0005)     # 中等速度 (5kHz)

    print("电机控制序列完成")

except KeyboardInterrupt:
    print("\n程序被用户中断")
finally:
    # 清理GPIO资源
    step_pin.value = 0  # 确保PWM停止
    step_pin.close()
    dir_pin.close()
    print("GPIO资源已释放")