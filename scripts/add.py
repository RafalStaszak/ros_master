#!/usr/bin/env python
from ros_master.srv import *

import rospy


def handle_numbers(req):
    return TwoNumbersResponse(req.a + req.b)


def numbers_server():
    rospy.init_node('add_server')
    s = rospy.Service('add', TwoNumbers, handle_numbers)
    rospy.spin()


if __name__ == "__main__":
    numbers_server()
