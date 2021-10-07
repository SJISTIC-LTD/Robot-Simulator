# sensor gains (weights)
self.sensor_gains = [ 1.0+( (0.4*abs(p.theta)) / pi )
                      for p in supervisor.proximity_sensor_placements() ]

# ...

# return an obstacle avoidance vector in the robot's reference frame
# also returns vectors to detected obstacles in the robot's reference frame
def calculate_ao_heading_vector( self ):
  # initialize vector
  obstacle_vectors = [ [ 0.0, 0.0 ] ] * len( self.proximity_sensor_placements )
  ao_heading_vector = [ 0.0, 0.0 ]             
  
  # get the distances indicated by the robot's sensor readings
  sensor_distances = self.supervisor.proximity_sensor_distances()
  
  # calculate the position of detected obstacles and find an avoidance vector
  robot_pos, robot_theta = self.supervisor.estimated_pose().vector_unpack()
  
  for i in range( len( sensor_distances ) ):
    # calculate the position of the obstacle
    sensor_pos, sensor_theta = self.proximity_sensor_placements[i].vector_unpack()
    vector = [ sensor_distances[i], 0.0 ]
    vector = linalg.rotate_and_translate_vector( vector, sensor_theta, sensor_pos )
    obstacle_vectors[i] = vector   # store the obstacle vectors in the robot's reference frame
    
    # accumulate the heading vector within the robot's reference frame
    ao_heading_vector = linalg.add( ao_heading_vector,
                                 linalg.scale( vector, self.sensor_gains[i] ) )
                                 
  return ao_heading_vector, obstacle_vectors
