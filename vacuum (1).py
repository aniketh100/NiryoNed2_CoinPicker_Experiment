from niryo_robot_python_ros_wrapper import *
import rospy

rospy.init_node("niryo_ned")

bot = NiryoRosWrapper()

#
workspace_name = "gazebo_1"

bot.set_learning_mode(True)

bot.calibrate_auto()


#
observation_pose = (0.174, 0., 0.211, 3.137, 1.478, 3.137)
#observation_pose = (0., 0., 0., 0., 1., -1.)
placingPose = (0., 0.25, 0.1, 0., 1.57, 1.57)


#
bot.move_to_sleep_pose()
#bot.setup_electromagnet()

while(True):

	bot.move_pose(*observation_pose)

	ret = bot.move_to_object(workspace_name, 0, ObjectShape.ANY, ObjectColor.ANY)
	obj_found, obj_shape, obj_col = ret

	#x,y,z,r,p,y = obj_pose
	#objPose = [x,y,z,r,p,y]
	objPose = bot.get_pose_as_list()

	#bot.move_pose(*observation_pose)
	if obj_found:
		bot.pick_from_pose(objPose[0],objPose[1],objPose[2],objPose[3],objPose[4],objPose[5])
		bot.place_from_pose(placingPose[0],placingPose[1],placingPose[2],placingPose[3],placingPose[4],placingPose[5])

		#bot.activate_electromagnet('''pin id here''')
		#bot.move_pose(*place_pose)
		#bot.deactivate_electromagnet('''pin id here''')

'''
for i in range(0,5):
	bot.move_pose(*observation_pose)
# Trying to pick target using camera
	ret = bot.vision_pick(workspace_name,
                              height_offset=0,
                              shape=ObjectShape.ANY,
                              color=ObjectColor.ANY)
	obj_found, shape_ret, color_ret = ret
	if obj_found:
    		bot.place_from_pose(*place_pose)
'''
bot.end()
