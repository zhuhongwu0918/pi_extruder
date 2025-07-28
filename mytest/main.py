import logging
import sys
import os
import app_ui
from main_application import MainApplication
import signal
# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
def signal_handler(sig, frame):
    logging.warning("捕获到Ctrl+C信号")
    app.safe_shutdown()

if __name__ == "__main__":
    app = MainApplication()
    # 设置Ctrl+C信号处理
    try:
        signal.signal(signal.SIGINT, signal_handler)
    except ImportError:
        pass  # Windows系统可能需要额外的处理
    # 运行主循环
    app.mainloop()
    # 确保完全退出
    os._exit(0)