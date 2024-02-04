#!/usr/bin/env python3


import rospy
import smach

from go_to_normaljoints import GO_TO_NORMAL


#Define the idle state
class Idle(smach.State):
    def __init__(self):
        smach.State.__init__(self,outcomes = ['Start',"Stay Idle"])
    
    def execute(self,userdata):
        user = input("Do you want to start the machine:(y/n) ")
        if user == "y":
            return "Start"
        else:
            return "Stay Idle"
        
