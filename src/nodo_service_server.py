#!/usr/bin/env python3
import rospy
from package_robot.srv import SumaTwoInts, SumaTwoIntsResponse

def handle_suma_two_ints(req):
    print ("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return SumaTwoIntsResponse(req.a+req.b)

def nodo():
    rospy.init_node('nodo_suma_two_ints_server')

    s = rospy.Service('suma_two_ints',SumaTwoInts, handle_suma_two_ints)
    print("ready to add two ints.")
    rospy.spin()

   

if __name__ == '__main__':
    try:
        nodo()
    except rospy.ROSInterruptException:
        pass