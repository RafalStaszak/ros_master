#!/usr/bin/env python
from ros_master.srv import *

import rospy


def handle_numbers(req):
    try:
        return TwoNumbersResponse(req.a / req.b)
    except ZeroDivisionError:
        return TwoNumbersResponse(float('nan'))


def numbers_server():
    rospy.init_node('divide_server')
    s = rospy.Service('divide', TwoNumbers, handle_numbers)
    rospy.spin()


if __name__ == "__main__":
    numbers_server()
