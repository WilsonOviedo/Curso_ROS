#!/usr/bin/env python3
import rospy

def nodo():
    rospy.init_node('nodo1')

    mensaje = "Hola mundo"

    rospy.loginfo(mensaje)

if __name__ == '__main__':
    try:
        nodo()
    except rospy.ROSInterruptException:
        pass