#!/usr/bin/env python3
import rospy
from package_robot.srv import SumaTwoInts

def add_two_ints_client(x,y):
    rospy.wait_for_service('suma_two_ints')

    try:
        add_two_ints = rospy.ServiceProxy('suma_two_ints', SumaTwoInts)
        resp = add_two_ints(x,y)
        return resp.sum 
    except rospy.ServiceException as e :
        print("Service call failes : %s" %e)

def nodo():
    rospy.init_node('nodo_suma_two_ints_client')
    x = 7
    y =8
    print("Requesting %s + %s"%(x,y))
    print("%s + %s = %s"%(x,y, add_two_ints_client(x,y)))
    

   

if __name__ == '__main__':
    try:
        nodo()
    except rospy.ROSInterruptException:
        pass