                                                               RESEARCH TRACK - 1
                                                                  ASSIGNMENT 2
NAME:NIVA BINESH
REG:NO:5061518
TOPIC:mobile robot controller
YEAR:2020/2021
PROFESSOR:Carmine Tommaso Recchiuto, Phd

ASSIGNMENT DESCRIPTION:
            This assignment aims to develope an architecture inorder to control the motion of a mobile robot. Here the simulation is done with the help of gazebo.


### Robot behaviour

The robot behavior can be defined by selecting from the user interface, among the six possible choices below:
- 1, Robot will move to a random destination chosen from six different coordinates provided.
- 2, Robot reaches a desired position from the a set choice given to the user.
- 3, Robot finds a closer wall and start moving along the wall, until the time set by the user.
- 4, Robot stays still at the current position for a given time.
- 5, Robot changes the planning algorithm between the dijkstra's and the 'bug0' one.
          

CODE EXECUTION AND DEPENDENCIES:

          At first, gitclone the assignment from the link (GIT LINK) inside the /src folder of your ros workspace.The script is coded in python here. We need to make the nodes executable before running the code, using the following commands:
          
                  $ chmod +x bug_m.py
                  $ chmod +x bug_m2.py
                  $ chmod +x go_to_point_service_m.py
                  $ chmod +x position_server.py
                  $ chmod +x user_interface.py
                  $ chmod +x wall_follow_service.py

          After the making the nodes executable,re build the workspace with the command:
          
                  $ catkin_make

         
 	After building our workspace, we can run the assignment by using 'roslaunch' command. Here,the nodes are called altogether (we should create a seperate launchfile in which we include the node names and path for the final execution) in a single call.
          
          
                 # roslaunch final_assignment simulation_gmapping.launch

                 # roslaunch final_assignment final_launcher.launch

          In this command "final_assignment" defines the complete package and "simulation_gmapping.launch" define the launch file in which we have decleared the name and path of the individual nodes of our workspace. 

The outputs are attached below for the reference:

- 1, Robot moving to a random destination (chosen from six different coordinates provided).


- 2, Robot reaching a desired position (from the a set choice given to the user).


- 3, Robot finding a closer wall and start moving along the wall (until the time set by the user).


- 4, Robot staying still at the current position for a given time.



RQT_graph:


           
 
               
          
           
 
                  
 
          
                                                                      
