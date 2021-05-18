#!/usr/bin/env python3
import rospy
# from sensor_msgs.msg import JointState
from control_msgs.msg import JointControllerState
from std_msgs.msg import Float64

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.position[0])
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    rospy.loginfo("I heard %s", data.process_value)
    
def listener():

    rospy.init_node('listener', anonymous=True)

    # rospy.Subscriber('/lidar/joint_states', JointState, callback)
    # rospy.Subscriber('/lidar/joint1_position_controller/command', Float64, callback)
    rospy.Subscriber('/lidar/joint1_position_controller/state', JointControllerState, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
