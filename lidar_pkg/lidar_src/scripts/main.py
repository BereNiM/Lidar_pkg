#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math

def lidar_talker():
    pub = rospy.Publisher('/lidar/joint1_position_controller/command', Float64, queue_size=10)
    rospy.init_node('lidar_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #position = math.pi/3
        position = 3.14 * math.sin(rospy.get_time()/100*5)
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

if __name__ == '__main__':
    try:
        lidar_talker()
    except rospy.ROSInterruptException:
        pass
        
