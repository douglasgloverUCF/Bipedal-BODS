# from adafruit_servokit import ServoKit
from Resources import convert_angle, map
import math
from time import sleep

length = 1 # length of leg part (set to clarify units)

# Settings of gait
r = length # radius of gait shape (can become a function later if we choose)
# position of gait shape's center
xPos = 0 
yPos = -math.sqrt(3) * length
# returns x position of ankle joint relative to hip joint
def fx(theta):
    x = r * math.cos(theta) # x function of gait 
    return x + xPos
# returns y position of ankle joint relative to hip joint
def fy(theta):
    y = r / 2 * math.sin(theta) + abs(r / 2 * math.sin(theta)) # y function of gait
    return y + yPos



# returns distance between ankle joint and hip joint
def stretchDis(theta):
    xsq = math.pow(fx(theta), 2)
    ysq = math.pow(fy(theta), 2)
    return math.sqrt(xsq + ysq)

# returns target angle of knee in radians
def kneeAngle(theta):
    dis = stretchDis(theta)
    return math.pi - math.asin((dis / 2) / r) * 2 + math.pi/2 # 90 is pointing lower leg straight

# returns target angle of hip in radians
def hipAngle(theta):
    dis = stretchDis(theta)
    return math.acos((dis / 2) / r) + math.pi/2 # 90 is pointing upper leg straight

# kit = ServoKit(channels=16)
hip = 1
knee = 2
foot = 3
theta = 0

while(True):
    theta += 1
    if (theta > 360):
        theta = 0
    
    thetaRad = math.radians(theta)

    sleep(0.2)
    # kit.servo[hip].angle = map(math.degrees(hipAngle(theta)),0,270,0,180) 
    # kit.servo[knee].angle = map(math.degrees(kneeAngle(thetaRad)),0,270,0,180) 
    # kit.servo[foot].angle = map(math.degrees(hipAngle(thetaRad)),0,270,0,180)
    print("\nTheta =          " + str(theta))
    print("Hip Angle =      " + str(math.degrees(hipAngle(thetaRad))))
    print("Knee Angle =     " + str(math.degrees(kneeAngle(thetaRad))))
    print("Leg span =       " + str(stretchDis(thetaRad)))
