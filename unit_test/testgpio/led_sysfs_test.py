import time

def control_led(state):
    with open("/sys/class/leds/ACT/brightness", "w") as f:
        f.write("1" if state else "0")

# 测试LED闪烁
for _ in range(5):
    control_led(True)  # 亮
    time.sleep(0.5)
    control_led(False) # 灭
    time.sleep(0.5)