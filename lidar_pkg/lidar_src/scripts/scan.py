#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

def callback(data):

    rospy.loginfo(data.ranges)
    r = data.ranges
    n = len(r)
    x = []
    y = []
    angle  = np.pi * 2/n
    i = 0
    while i < n :
        x.append(r[i] * np.cos(angle * i))
        y.append(r[i] * np.sin(angle * i))
        i =i+1

    plt.plot(x,y,"r*")
    plt.show()

def listener():
 
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/lidar/laser/scan', LaserScan, callback)
    rospy.spin()
    
if __name__ == '__main__':
    listener()