from threading import Thread, Event
import logging
import time

class ProximitySensor(Thread):
    def __init__(self, stop_event, status_queue):
        super().__init__(name="SensorThread")
        self.stop_event = stop_event
        self.status_queue = status_queue
        
    def run(self):
        logging.info("接近开关线程启动")
        try:
            counter = 0
            while not self.stop_event.is_set():
                # 模拟传感器检测
                counter += 1
                sensor_status = f"检测到物体 #{counter}"
                self.status_queue.put(("sensor", sensor_status))
                time.sleep(1.2)
        finally:
            logging.info("接近开关线程安全退出")
