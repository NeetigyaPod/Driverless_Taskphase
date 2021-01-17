#!/usr/bin/env python3
from beginner_tutorials.msg import Addtwoints as AddTwoInts
import rospy


def add_two_ints():
    rospy.init_node('add_two_ints_input',anonymous=True)
    mes=AddTwoInts()
    while not rospy.is_shutdown():
    	mes.a=int(input("Enter first number"))
    	mes.b=int(input("Enter second number"))
    	pub = rospy.Publisher('addints', AddTwoInts,queue_size=10)
    	pub.publish(mes)

if __name__ == "__main__":
    add_two_ints()
