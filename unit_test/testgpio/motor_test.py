import RPi.GPIO as GPIO
import time

# 引脚定义 (BCM编号)
IN1, IN2, IN3, IN4 = 20, 21, 12, 16

def setup():
    GPIO.setmode(GPIO.BCM)
    pins = [IN1, IN2, IN3, IN4]
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
    print("GPIO setted!")

def forward(delay, steps):  # 正转
    print("Enter forward!")
    seq = [[1,0,1,0], [0,1,1,0], [0,1,0,1], [1,0,0,1]]
    for _ in range(steps):
        for step in seq:
            for i, pin in enumerate([IN1, IN2, IN3, IN4]):
                GPIO.output(pin, step[i])
            time.sleep(delay)

    print("Exit forward!")

try:
    setup()
    forward(0.001, 1600)  # 转1圈（1600脉冲/圈）
except KeyboardInterrupt:
    print("\n测试停止")

finally:
    GPIO.cleanup()                       # 清理GPIO设置