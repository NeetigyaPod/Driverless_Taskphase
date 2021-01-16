#!/usr/bin/env python3
import rospy
from beginner_tutorials.msg import Person as message

def AskTheClient():
	pub=rospy.Publisher('voteenquiry', message)
	rospy.init_node('votepublisher',anonymous=True)
	while not rospy.is_shutdown():
		Name=input("Enter name or press q to quit")
		if(Name=="q"):
			break
		Age=int(input("enter age"))
		messagepassed=message(Name,Age)
		pub.publish(messagepassed)
if __name__=='__main__':
	AskTheClient()
