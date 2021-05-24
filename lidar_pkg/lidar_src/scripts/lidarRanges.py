#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from control_msgs.msg import JointControllerState
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class Visualiser:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ln, = plt.plot([0.0], [0.0], 'ro')
        
        self.ln, = plt.plot([], [], 'r-')
        self.x_data, self.y_data = [] , []
        self.t = 0
        self.ln2, = plt.plot([], [], 'b*')
        self.px_data, self.py_data  = [] , []

        rospy.Subscriber('/lidar/joint1_position_controller/state', JointControllerState, self.callback)

    def plot_init(self):
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        return self.ln  

    def update_plot(self, frame):
        self.ln.set_data(self.x_data,self.y_data)
        self.ln2.set_data(self.px_data,self.py_data)
        return [self.ln, self.ln2]

    def lidar_callback(self,scan):
        r = scan.ranges
        n = len(r)
        x = []
        y = []
        angle  = np.pi * 2/n
        i = 0
        while i < n :
            x.append(r[i] * np.cos(angle * i))
            y.append(r[i] * np.sin(angle * i))
            i =i+1
        self.x_data = x
        self.y_data = y 

    def callback(self,data):
        angle  = data.process_value
        self.px_data = 1 * np.sin(angle)
        self.py_data = 1 * np.cos(angle)        


rospy.init_node('listener')
vis = Visualiser()
sub = rospy.Subscriber('/lidar/laser/scan', LaserScan, vis.lidar_callback)
ani = FuncAnimation(vis.fig, vis.update_plot, init_func=vis.plot_init)
plt.show(block=True) 
