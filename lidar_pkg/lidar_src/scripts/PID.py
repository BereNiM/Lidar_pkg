#!/usr/bin/env python3
# license removed for brevity
import rospy
from control_msgs.msg import JointControllerState
import math

def lidar_PID1():
    pub = rospy.Publisher('/lidar/joint1_position_controller/state', JointControllerState, queue_size=10)
    rospy.init_node('lidar_PID1', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #position = math.pi/3
        position = 1.5
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

if __name__ == '__main__':
    try:
        lidar_talker()
    except rospy.ROSInterruptException:
        pass
        
