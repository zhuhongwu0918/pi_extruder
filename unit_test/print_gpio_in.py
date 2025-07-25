'''
高级GPIO测试模式启动 (使用GPIO Zero库)
状态记录保存到 gpio_status.log
按Ctrl+C退出程序

上限开关: GPIOGPIO17 (内部上拉: True)
下限开关: GPIOGPIO27 (内部上拉: True)
--------------------------------------------------
初始状态: 上限[OPEN] 下限[OPEN]

实时监控中...
当前状态: 上限[OPEN] 下限[OPEN]N]
'''
from gpiozero import DigitalInputDevice
import time
import logging
from datetime import datetime
from signal import pause

# 引脚定义
UPPER_LIMIT_PIN = 17    # 上限开关 (BCM 17, 物理引脚11)
LOWER_LIMIT_PIN = 27    # 下限开关 (BCM 27, 物理引脚13)

# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    filename='gpio_status.log',
    filemode='w'
)

# 创建开关设备对象
upper_limit = DigitalInputDevice(
    UPPER_LIMIT_PIN, 
    pull_up=True, 
    bounce_time=0.05  # 50ms去抖
)

lower_limit = DigitalInputDevice(
    LOWER_LIMIT_PIN, 
    pull_up=True, 
    bounce_time=0.05
)

def log_status():
    """记录当前状态到日志"""
    upper = "TRIGGERED" if upper_limit.is_active else "OPEN"
    lower = "TRIGGERED" if lower_limit.is_active else "OPEN"
    return upper, lower

def status_change_handler(device, status_name):
    """处理状态变化的回调函数"""
    global last_upper, last_lower, start_time
    
    current_upper, current_lower = log_status()
    
    # 仅当状态确实改变时才记录
    if (current_upper != last_upper) or (current_lower != last_lower):
        duration = time.time() - start_time
        logging.info(
            f"状态变化: {duration:.3f}s, "
            f"上限: {last_upper} -> {current_upper}, "
            f"下限: {last_lower} -> {current_lower}"
        )
        
        # 更新状态跟踪变量
        last_upper, last_lower = current_upper, current_lower
        start_time = time.time()

try:
    print("高级GPIO测试模式启动 (使用GPIO Zero库)")
    print("状态记录保存到 gpio_status.log")
    print("按Ctrl+C退出程序\n")
    
    # 打印引脚信息
    print(f"上限开关: GPIO{upper_limit.pin} (内部上拉: {upper_limit.pull_up})")
    print(f"下限开关: GPIO{lower_limit.pin} (内部上拉: {lower_limit.pull_up})")
    print("-" * 50)
    
    # 初始状态
    last_upper, last_lower = log_status()
    start_time = time.time()
    
    # 记录初始状态
    logging.info(f"初始状态 - 上限: {last_upper}, 下限: {last_lower}")
    print(f"初始状态: 上限[{last_upper}] 下限[{last_lower}]")
    
    # 注册状态变化回调
    upper_limit.when_activated = lambda: status_change_handler(upper_limit, "上限")
    upper_limit.when_deactivated = lambda: status_change_handler(upper_limit, "上限")
    lower_limit.when_activated = lambda: status_change_handler(lower_limit, "下限")
    lower_limit.when_deactivated = lambda: status_change_handler(lower_limit, "下限")
    
    # 实时状态显示
    print("\n实时监控中...")
    while True:
        current_upper, current_lower = log_status()
        print(f"当前状态: 上限[{current_upper}] 下限[{current_lower}]", end='\r')
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n\n测试结束 - 正在清理资源...")
finally:
    # 关闭设备释放资源
    upper_limit.close()
    lower_limit.close()
    print("GPIO资源已安全释放")