from random import randint
from time import sleep
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

while(True):
    const = randint(1,179)
    kit.servo[3].angle = const
    print("Rotating to : " + str(int))
    sleep(2)
