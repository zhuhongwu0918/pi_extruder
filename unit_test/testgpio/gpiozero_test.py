#https://www.raspberrypi.com/documentation/computers/os.html#introduction
from gpiozero import LED
from time import sleep

led = LED(17)

# while True:
    # led.on()
    # sleep(1)
    # led.off()
    # sleep(1)

for i in range(10):
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    print(i)
