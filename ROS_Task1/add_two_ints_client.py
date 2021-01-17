#!/usr/bin/env python

from __future__ import print_function
import sys
import rospy
from beginner_tutorials.msg import Addtwoints as AddTwoInts
def output(mes):
   rospy.loginfo(mes.a+mes.b)

def add_two_ints():
    rospy.init_node('add_two_ints_client',anonymous=True)
    rospy.Subscriber('addints',AddTwoInts,output)
    rospy.spin()



if __name__ == "__main__":
    add_two_ints()

#a
