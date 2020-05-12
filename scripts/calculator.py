#!/usr/bin/env python
import re
import rospy
from ros_master.srv import *


def add(x, y):
    rospy.wait_for_service('add')
    try:
        proxy = rospy.ServiceProxy('add', TwoNumbers)
        resp1 = proxy(x, y)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


def subtract(x, y):
    rospy.wait_for_service('subtract')
    try:
        proxy = rospy.ServiceProxy('subtract', TwoNumbers)
        resp1 = proxy(x, y)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


def multiply(x, y):
    rospy.wait_for_service('multiply')
    try:
        proxy = rospy.ServiceProxy('multiply', TwoNumbers)
        resp1 = proxy(x, y)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


def divide(x, y):
    rospy.wait_for_service('divide')
    try:
        proxy = rospy.ServiceProxy('divide', TwoNumbers)
        resp1 = proxy(x, y)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


def solve(equation):
    numbers = re.split("[\+\-\*\/]", equation)
    numbers = list(map(lambda x: float(x), numbers))

    signs = re.sub("\d+(\.\d+)?", '', equation)
    signs.join('')
    signs = list(filter(lambda x: x != '', signs))


    while '*' in signs or '/' in signs:
        for i, sign in enumerate(signs):
            left = i
            right = i + 1
            if sign == '*':
                result = multiply(numbers[left], numbers[right])
                signs.pop(i)
                numbers.pop(right)
                numbers[left] = result
            if sign == '/':
                result = divide(numbers[left], numbers[right])
                signs.pop(i)
                numbers.pop(right)
                numbers[left] = result

    while '+' in signs or '-' in signs:
        for i, sign in enumerate(signs):
            left = i
            right = i + 1
            if sign == '+':
                result = add(numbers[left], numbers[right])
                signs.pop(i)
                numbers.pop(right)
                numbers[left] = result
            if sign == '-':
                result = subtract(numbers[left], numbers[right])
                signs.pop(i)
                numbers.pop(right)
                numbers[left] = result

    return numbers[0]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        equation = sys.argv[1]
        print solve(equation)
