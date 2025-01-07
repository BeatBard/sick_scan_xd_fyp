#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

def fix_frame_id(scan_msg):
    # Override the frame_id
    scan_msg.header.frame_id = "laser_frame"
    pub.publish(scan_msg)

if __name__ == "__main__":
    rospy.init_node("fix_frame_id_node")
    pub = rospy.Publisher("/fixed_scan", LaserScan, queue_size=10)
    rospy.Subscriber("/scan", LaserScan, fix_frame_id)
    rospy.spin()
