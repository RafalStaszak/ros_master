#!/usr/bin/env python

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import time


def image_publisher():
    pub = rospy.Publisher('/image', Image)
    time.sleep(1.0)
    image_path = rospy.get_param('image_path')
    scale = rospy.get_param('scale')
    image = cv2.imread(image_path)
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    image = cv2.resize(image, (width, height))
    message = CvBridge().cv2_to_imgmsg(image)
    pub.publish(message)
    print 'Image published'

if __name__ == '__main__':
    rospy.init_node('image_publisher')
    try:
        image_publisher()
    except rospy.ROSInterruptException:
        pass
