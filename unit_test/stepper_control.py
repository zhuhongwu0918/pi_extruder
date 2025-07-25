#!/usr/bin/env python3
import time
import gpiozero as gpio

# 定义GPIO引脚
PULSE_PIN = 18    # GPIO18 (PWM0) - 脉冲信号
DIRECTION_PIN = 20  # GPIO20 - 方向信号
ENABLE_PIN = 21     # GPIO21 - 使能信号

# DM542驱动器配置
PULSES_PER_REVOLUTION = 400  # 驱动器上标记的Pulse/rev值
ROTATION_TIME = 6.0          # 旋转一圈所需时间（秒）

def main():
    try:
        # 初始化GPIO引脚
        pulse = gpio.PWMOutputDevice(PULSE_PIN, active_high=False, initial_value=False)
        direction = gpio.OutputDevice(DIRECTION_PIN, active_high=False, initial_value=False)
        enable = gpio.OutputDevice(ENABLE_PIN, active_high=False, initial_value=True)
        
        print("步进电机控制系统已启动")
        print(f"配置: {PULSES_PER_REVOLUTION} 脉冲/圈, {ROTATION_TIME}秒/圈")
        
        # 计算脉冲频率 (Hz)
        pulse_frequency = PULSES_PER_REVOLUTION / ROTATION_TIME
        print(f"设置脉冲频率: {pulse_frequency:.2f} Hz")
        
        # 启用驱动器
        enable.off()  # 共阴极接法下，低电平启用
        print("驱动器已启用")
        
        # 设置方向（高电平为一个方向，低电平为另一个方向）
        direction.on()  # 设置旋转方向
        print("方向已设置")
        
        # 开始发送脉冲
        pulse.value = 0.5  # 50%占空比
        pulse.frequency = pulse_frequency
        print(f"电机开始旋转，{ROTATION_TIME}秒/圈")
        
        # 让电机旋转指定时间
        rotation_duration = 2  # 旋转30秒
        start_time = time.time()
        
        while time.time() - start_time < rotation_duration:
            elapsed = time.time() - start_time
            remaining = rotation_duration - elapsed
            print(f"\r旋转中: {elapsed:.1f}秒 / {rotation_duration:.1f}秒 (剩余: {remaining:.1f}秒)", end='')
            time.sleep(0.1)
        
        print("\n旋转完成")
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    finally:
        # 清理GPIO资源
        if 'pulse' in locals():
            pulse.off()
            pulse.close()
        if 'direction' in locals():
            direction.off()
            direction.close()
        if 'enable' in locals():
            enable.on()  # 禁用驱动器
            enable.close()
        print("GPIO资源已清理")

if __name__ == "__main__":
    main()    