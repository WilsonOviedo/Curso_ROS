#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(mensaje):
    rospy.loginfo("I heard %s",mensaje.data)

def nodo():
    rospy.init_node('nodo_subscriber')

    pub = rospy.Subscriber('example',String, callback)

    rospy.spin()

   

if __name__ == '__main__':
    try:
        nodo()
    except rospy.ROSInterruptException:
        pass