import pigpio
import time

# 初始化pigpio（连接本地pigpiod服务）
pi = pigpio.pi()

# 定义GPIO引脚（BCM编号）
LED_PIN = 17  # 替换为您要控制的引脚

try:
    # 设置引脚为输出模式
    pi.set_mode(LED_PIN, pigpio.OUTPUT)
    
    print("LED闪烁测试开始（按Ctrl+C停止）")
    while True:
        pi.write(LED_PIN, 1)  # 打开LED
        time.sleep(0.5)
        pi.write(LED_PIN, 0)  # 关闭LED
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n测试停止")

finally:
    pi.write(LED_PIN, 0)       # 确保LED关闭
    pi.stop()                  # 断开与pigpiod的连接