import threading as tr
import time as t
def while_true():
    for i in range(9):
        print("ooooohhhhhhhhhhhh"+str(i))
        t.sleep(1)

print("2333")

runT= tr.Thread(target=while_true)
runT.start()

print('end')