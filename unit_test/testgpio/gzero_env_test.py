#!/usr/bin/env python3
"""
树莓派5 LED控制测试
"""

import time
import sys
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

def main():
    print("=== 树莓派5 LED测试 ===")
    
    # 尝试不同方法
    methods = [
        {"name": "方法1: 使用ACT+PiGPIOFactory", "device": LED("ACT", pin_factory=PiGPIOFactory())},
        {"name": "方法2: 使用led0", "device": LED("led0", pin_factory=PiGPIOFactory())},
        {"name": "方法3: 使用InternalLED", "device": LED("ACT")}
    ]
    
    for method in methods:
        print(f"\n尝试 {method['name']}")
        led = method['device']
        
        try:
            # 测试闪烁
            for i in range(3):
                led.on()
                print(f"  LED ON ({i+1})")
                time.sleep(0.3)
                led.off()
                print(f"  LED OFF ({i+1})")
                time.sleep(0.3)
                
            print("  ✅ 测试成功!")
            return 0
            
        except Exception as e:
            print(f"  ❌ 失败: {str(e)}")
            continue
    
    print("\n所有方法均失败，尝试直接sysfs控制...")
    try:
        for i in range(5):
            with open('/sys/class/leds/ACT/brightness', 'w') as f:
                f.write('1')
            print(f"  LED ON ({i+1})")
            time.sleep(0.3)
            
            with open('/sys/class/leds/ACT/brightness', 'w') as f:
                f.write('0')
            print(f"  LED OFF ({i+1})")
            time.sleep(0.3)
            
        print("  ✅ Sysfs控制成功!")
        return 0
    except Exception as e:
        print(f"  ❌ 最终失败: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())