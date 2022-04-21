# from adafruit_servokit import ServoKit
from Resources import convert_angle, map
import math
from time import sleep

length = 6.402 # length of leg part (in inches)

# Settings of gait
r = 0.6 # radius of gait shape (can become a function later if we choose)
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
    # y = 0
    return y + yPos


# returns distance between ankle joint and hip joint
def stretchDis(theta):
    xsq = math.pow(fx(theta), 2)
    ysq = math.pow(fy(theta), 2)
    return math.sqrt(xsq + ysq)

# returns target angle of knee in radians
def kneeAngle(theta):
    dis = stretchDis(theta)
    return 3 * math.pi/2 - math.asin((dis / 2) / length) * 2 # 90 is pointing lower leg straight

# returns target angle of hip in radians
def hipAngle(theta):
    dis = stretchDis(theta)
    return math.acos((dis / 2) / length) + math.pi/2 # 90 is pointing upper leg straight

#kit = ServoKit(channels=16)
hip = 1
knee = 2
hip2 = 3
knee2 = 4
theta = 0

while(True):
    theta += 1
    if (theta > 360):
        theta = 0
    
    thetaRad = math.radians(theta)
    thetaRad2 = math.radians(theta + 180)


    hipangle = map(math.degrees(hipAngle(thetaRad)),0,270,0,180) 
    kneeangle = map(math.degrees(kneeAngle(thetaRad)),0,270,0,180) 
    hipangle2 = map(math.degrees(hipAngle(thetaRad2)),0,270,0,180) 
    kneeangle2 = map(math.degrees(kneeAngle(thetaRad2)),0,270,0,180) 

    sleep(0.01)
    #kit.servo[hip].angle = hipangle 
    #kit.servo[knee].angle = kneeangle
    #kit.servo[hip2].angle = hipangle2
    #kit.servo[knee2].angle = kneeangle2
    print("\nTheta =          " + str(theta))
    print("Hip Angle =      " + str(hipangle))
    print("Knee Angle =     " + str(kneeangle))
    print("Hip Angle2 =      " + str(hipangle2))
    print("Knee Angle2 =     " + str(kneeangle2))
    print("Leg span =       " + str(stretchDis(thetaRad)))