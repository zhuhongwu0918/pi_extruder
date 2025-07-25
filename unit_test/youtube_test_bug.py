# Note: You also have to setup the TB6600 switches On for 2,5 and 6. i.e. 2.5A  max with 12V it works fine.
# Cannot determine SOC peripheral base address
from time import sleep
import RPi.GPIO as GPIO
DIR = 20
STEP = 21
CW = 1
CCW = 0
SPR = 1600

GPIO.setwarnings(False)
GPIO.RPI_REVISION = 3  # 关键：指定树莓派型号（3=4B, 4=400, 5=Zero 2W等）

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
delay = 0.001

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP,GPIO.LOW)
    sleep(delay)

delay = 0.0001
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP,GPIO.LOW)
    sleep(delay)

delay = 0.00008
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP,GPIO.LOW)
    sleep(delay)

delay = 0.00004
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP,GPIO.LOW)
    sleep(delay)

delay = 0.00002
for x in range(8000):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP,GPIO.LOW)
    sleep(delay)

delay = 0.00001
for x in range(16000):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP,GPIO.LOW)
    sleep(delay)

delay = 0.00007
for x in range(32000):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP,GPIO.LOW)
    sleep(delay)
    
GPIO.cleanup()