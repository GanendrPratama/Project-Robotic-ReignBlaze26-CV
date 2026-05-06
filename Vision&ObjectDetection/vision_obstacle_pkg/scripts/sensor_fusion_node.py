#!/usr/bin/env python3

import rospy
from vision_obstacle_pkg.msg import ObjectDistance

def main():
    rospy.init_node('sensor_fusion_node', anonymous=True)
    rospy.loginfo("Starting Sensor Fusion Node...")
    
    pub_dist = rospy.Publisher('/vision/object_distance', ObjectDistance, queue_size=10)
    
    # TODO: Subscribe to Depth image (/camera/depth/image_raw)
    # TODO: Subscribe to Bounding Boxes from object_detect_node
    # TODO: Calculate average depth inside bounding box
    
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
