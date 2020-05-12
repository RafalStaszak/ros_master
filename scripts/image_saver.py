#!/usr/bin/env python

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import os

i = 0


def image_saver(data):
    global i
    image = CvBridge().imgmsg_to_cv2(data)
    save_dir = rospy.get_param('save_dir')
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    cv2.imwrite(os.path.join(save_dir, "{0:04d}.png".format(i)), image)
    print('Image saved!')


if __name__ == '__main__':
    rospy.init_node('image_saver')
    sub = rospy.Subscriber('/image', Image, image_saver)
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
