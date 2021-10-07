# return a go-to-goal heading vector in the robot's reference frame
def calculate_gtg_heading_vector( self ):
  # get the inverse of the robot's pose
  robot_inv_pos, robot_inv_theta = self.supervisor.estimated_pose().inverse().vector_unpack()
  
  # calculate the goal vector in the robot's reference frame
  goal = self.supervisor.goal()
  goal = linalg.rotate_and_translate_vector( goal, robot_inv_theta, robot_inv_pos )
  
  return goal
# calculate translational velocity
# velocity is v_max when omega is 0,
# drops rapidly to zero as |omega| rises
v = self.supervisor.v_max() / ( abs( omega ) + 1 )**0.5
