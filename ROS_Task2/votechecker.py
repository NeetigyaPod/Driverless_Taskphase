#!/usr/bin/env python3
import rospy
from beginner_tutorials.msg import Person as message
from beginner_tutorials.msg import output
def checker(mess):
	pub=rospy.Publisher('voteoutput',output,queue_size=10)
	msg=output()
	msg.voter=mess
	if(mess.Age>=18):
		msg.eligibility="Eligible"
	else:
		msg.eligibility="Not eligible"
	pub.publish(msg)

def Receiver():
	rospy.init_node('receiver',anonymous=True)
	rospy.Subscriber('voteenquiry', message, checker)
	rospy.spin()

if __name__=='__main__':
	Receiver()
