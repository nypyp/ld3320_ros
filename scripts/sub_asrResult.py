#! /usr/bin/env python
"""
    接收circle_asr.py话题
"""

import rospy
from std_msgs.msg import String

def doMsg(msg):
    rospy.loginfo("Detect result:%s",msg.data)

if __name__ == "__main__":
    rospy.init_node("listener_p")
    sub = rospy.Subscriber("VoiceDetect",String,doMsg,queue_size=10)
    rospy.spin()