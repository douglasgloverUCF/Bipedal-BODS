from adafruit_servokit import ServoKit
from Resources import convert_angle, map

# Servos can only rotate between "0 and 180" degrees
min = 0
max = 180

# Our servos can rotate between 0 and 270 degrees
#  thus, refer to this mapping function
map()


# use the mapping function to rotate the servos to the desired rotation
# map(angle,0,270,0,180) : Returns an acceptable angle that can be send to the servo handler


# writing about the servo handler:

# Init your servos like this,

# DO NOT CHANGE THIS (you can change the var name tho)
kit = ServoKit(channels=16)

# to spin a servo use the following

kit.servo[0].angle = 90

# where servo[0] is the number of the servo you want to rotate 0-16, and 90 is the angle between 0-270 that you want to rotate to (hence the mapping function)

#so a more common way you will be writing your servo rotation script is like so
servo = 1
angle = 210
kit.servo[servo].angle = map(angle,0,270,0,180)


#There is also a convert_angle func that you can use, but it just short hands the map function

servo = 2
angle = 244
kit.servo[servo].angle = convert_angle(angle)

#Both of these ways spin a servo some angle, but depends on the way you wish to shorthand

# from here, go crazy, think of ways to get the servos to spin, and come up with overly-complicated mathematical functions to handle it all!!
