from threading import Thread, Event
import logging
import time
class MotorController(Thread):
    def __init__(self, stop_event, status_queue):
        super().__init__(name="MotorThread")
        self.stop_event = stop_event
        self.status_queue = status_queue
        
    def run(self):
        logging.info("电机线程启动")
        try:
            while not self.stop_event.is_set():
                # 模拟电机工作
                motor_status = f"电机运行中... {time.strftime('%H:%M:%S')}"
                self.status_queue.put(("motor", motor_status))
                time.sleep(0.8)
        finally:
            logging.info("电机线程安全退出")