#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def nodo():
    rospy.init_node('nodo_publisher')

    pub = rospy.Publisher('example',String, queue_size=10)

    rate=rospy.Rate(10)

    while not rospy.is_shutdown():
        mensaje = "Nodo publisher"
        
        rospy.loginfo(mensaje)

        pub.publish(mensaje)

        rate.sleep()


if __name__ == '__main__':
    try:
        nodo()
    except rospy.ROSInterruptException:
        pass