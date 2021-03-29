# from threading import Thread
# from time import sleep
import queue

que=queue.Queue()
que.put("2333")
que.put("111")
print(que.get())
print(que.get())
print(que.get())
