# Note: You also have to setup the TB6600 switches On for 2,5 and 6. i.e. 2.5A max with 12V it works fine.

from time import sleep
from gpiozero import DigitalOutputDevice

# 引脚定义
DIR = 20
STEP = 21
CW = True   # gpiozero 使用布尔值 True/False 代替 1/0
CCW = False
SPR = 1600  # 每转步数

# 创建方向控制对象
dir_pin = DigitalOutputDevice(DIR)
# 创建步进脉冲控制对象
step_pin = DigitalOutputDevice(STEP)

# 设置旋转方向
dir_pin.value = CW

# 定义步进函数
def step_motor(steps, delay):
    for _ in range(steps):
        step_pin.on()   # 产生上升沿脉冲
        sleep(delay)
        step_pin.off()  # 产生下降沿
        sleep(delay)

# 执行不同速度的步进序列
step_motor(SPR, 0.001)    # 初始速度
step_motor(SPR*10, 0.0001)   # 加速
# step_motor(SPR, 0.00008)  # 继续加速
# step_motor(SPR, 0.00004)  # 高速
# step_motor(8000, 0.00002) # 超高速
# step_motor(16000, 0.00001) # 极限速度
# step_motor(32000, 0.00007) # 降速运行

# 清理GPIO资源
dir_pin.close()
step_pin.close()