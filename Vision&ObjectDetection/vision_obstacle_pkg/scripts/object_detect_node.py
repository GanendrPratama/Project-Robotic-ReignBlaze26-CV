#!/usr/bin/env python3

import rospy

def main():
    rospy.init_node('object_detect_node', anonymous=True)
    rospy.loginfo("Starting Object Detection Node...")
    
    # TODO: Initialize YOLO/TFLite model here
    # TODO: Subscribe to /camera/color/image_raw
    # TODO: Publish Bounding Boxes or custom messages
    
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
