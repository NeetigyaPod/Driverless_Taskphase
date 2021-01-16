#!/usr/bin/env python3
import rospy
from beginner_tutorials.msg import Person,output

def action(msg):
	rospy.loginfo("Name: "+msg.voter.Name)
	rospy.loginfo(msg.eligibility)
def OutputDo():
	rospy.init_node('output',anonymous=True)
	rospy.Subscriber('voteoutput',output,action)
	rospy.spin()
if __name__=='__main__':
	OutputDo()
