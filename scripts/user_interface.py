#! /usr/bin/env python

# import ros stuff
import rospy
import random
import time
from std_srvs.srv import *
from final_assignment.srv import Target


# service callback
target_array = [[-4,-3],[-4,2],[-4,7],[5,-7],[5,-3],[5,1]]

#Iitialize the client for requesting the target_id 
restart = rospy.ServiceProxy('rand_target_id', Target)
rospy.init_node('user_interface')

def user_interface(req):



    time.sleep(1)
    print("Choose the mode from the following:")
    print("[1] Move Robo to any random position among the given coordinates: [(-4,-3),(-4,2),(-4,7),(5,-7),(5,-3),(5,1)]")
    print("[2] Select a desired destination point from the following: [(-4,-3),(-4,2),(-4,7),(5,-7),(5,-3),(5,1)]")
    print("[3] Travel along the wall")
    print("[4] Stay still")
    print("[5] To change the plan")
    beh_int = int(raw_input('I :'))
   
    if beh_int < 3:
	
	x_old = rospy.get_param('des_pos_x')
	y_old = rospy.get_param('des_pos_y')
	x = x_old
        y = y_old
	min_id = 1
 	max_id = 6

	while x_old == x and y_old ==y:	
            if beh_int == 1:
		target = restart()
    	    	target_id = target.target_id
		print('Service called:')
		print(target_id) 
	        target = target_array[target_id-1]
            elif beh_int == 2:
	    	print("Select desired destination from- [(-4,-3),(-4,2),(-4,7),(5,-7),(5,-3),(5,1)]")
	    	print("Type corresponding number id for the above destination coordinates (between 1 and 6)")
            	tar_id = int(raw_input('Id :'))
	    	if tar_id < min_id or tar_id > max_id:
          	    print("Invalid entry selected") 
		    target = [x_old, y_old]		    	                   
		else:	
	    	    target = target_array[tar_id-1]
    	    x = float(target[0])
    	    y = float(target[1])
 	    if x_old == x and y_old == y:
	    	print("Hey there! Tell me the new destination.")    
	
	
    	rospy.set_param("des_pos_x", x)
    	rospy.set_param("des_pos_y", y)
	state = rospy.set_param('state_value', 0)
    	print("Okay, Let's go there!")	
	print(x,y)

    elif beh_int == 3: 
	       
	print("How many seconds should I travel along the wall?")
        wall_time = int(raw_input('w_t:'))
	print("Getting ready to travel along the wall for %d seconds." % wall_time)	
	rospy.set_param('target_time', wall_time)

	state = rospy.set_param('state_value', 3)
	
    elif beh_int == 4:
        print("How many seconds should I stay at this position?")
        wait_time = int(raw_input('w_t:'))
	print("Resting here for %d seconds." % wait_time)
	rospy.set_param('target_time', wait_time)
	state = rospy.set_param('state_value', 4)

    elif beh_int == 5:

	# Read the current algorithm active
	bug_status = rospy.get_param('bug_trigger')
	print(int(bug_status))
	if bug_status == 0:
	    print('Move_base disabled')
	    rospy.set_param('bug_trigger', 1)
	    print('Bug_0 enabled')
	else:
	    print('Bug_0 disabled')
	    rospy.set_param('bug_trigger', 0)
	    print('Move_base enabled')
	print(rospy.get_param('bug_trigger'))
	state = rospy.set_param('state_value', 5)

    return []

def main():
    
    
    x = rospy.get_param("des_pos_x")
    y = rospy.get_param("des_pos_y")
    print("Hi! Robo is moving to the first position: x = " +
        str(x) + ", y = " + str(y))
    rospy.Service('user_interface', Empty, user_interface)
    rate = rospy.Rate(20)

    while not rospy.is_shutdown(): 	
        rate.sleep()


if __name__ == '__main__':
    main()
