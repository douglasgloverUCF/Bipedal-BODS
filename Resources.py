'''
The mapping function allows you to take in some number x
   Then give in the range that x can reside in,
   Then give the range that x can return
    and this function will return the number "Y" which is the ratio of x to the new range


Example:

map(0,0,180,0,270) : OUTPUT : 0

map(180,0,180,0,270) : OUTPUT : 270

map(90,0,180,0,270) : OUTPUT : 135

Note! : If you import Resources.py, this function is referenced there
'''
def map(x, in_min, in_max, out_min, out_max):
    """Takes X and some range x should fall in between, then converts it linearly
    to the new range

    Args:
        x (int): Number to be mapped
        in_min (int): Lowest Interval X can be
        in_max (int): Maximum Interval X can be
        out_min (int): Lowest Interval X should reach
        out_max (int): Maximum Interval X should reach

    Returns:
        int: The number x, but converted to the new range
    """
    return float((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def convert_angle(angle):
    """Converts some ANGLE between 0-270 to acceptable servo values

    Args:
        angle (int): some angle 0-270 that should be converted

    Returns:
        int: some value mapped from 0-180 derived from angle
    """
    return map(angle,0,270,0,180)

