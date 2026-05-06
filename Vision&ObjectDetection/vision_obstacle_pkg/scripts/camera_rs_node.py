#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    rospy.init_node('camera_rs_node', anonymous=True)
    rospy.loginfo("Starting RealSense Camera Node...")
    
    # Placeholder for actual D435 initialization
    # pub_rgb = rospy.Publisher('/camera/color/image_raw', Image, queue_size=10)
    # pub_depth = rospy.Publisher('/camera/depth/image_raw', Image, queue_size=10)
    
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # TODO: Read from RealSense and publish Image messages
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
