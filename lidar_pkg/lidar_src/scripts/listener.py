#!/usr/bin/env python3
import rospy
# from sensor_msgs.msg import JointState
from control_msgs.msg import JointControllerState

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.position[0])
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.error)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    # rospy.Subscriber('/lidar/joint_states', JointState, callback)
    rospy.Subscriber('/lidar/joint1_position_controller/state', JointControllerState, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

