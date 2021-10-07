# step the simulation through one time interval
def step( self ):
dt = self.dt
# step all the robots
for robot in self.robots:
# step robot motion
robot.step_motion( dt )

# apply physics interactions
self.physics.apply_physics()

# NOTE: The supervisors must run last to ensure they are observing the "current" world
# step all of the supervisors
for supervisor in self.supervisors:
supervisor.step( dt )

# increment world time
self.world_time += dt
# generate and send the correct commands to the robot
def _send_robot_commands( self ):
  # ...
  v_l, v_r = self._uni_to_diff( v, omega )
  self.robot.set_wheel_drive_rates( v_l, v_r )

def _uni_to_diff( self, v, omega ):
  # v = translational velocity (m/s)
  # omega = angular velocity (rad/s)

  R = self.robot_wheel_radius
  L = self.robot_wheel_base_length

  v_l = ( (2.0 * v) - (omega*L) ) / (2.0 * R)
  v_r = ( (2.0 * v) + (omega*L) ) / (2.0 * R)

  return v_l, v_r
  # update the distances indicated by the proximity sensors
def _update_proximity_sensor_distances( self ):
    self.proximity_sensor_distances = [ 0.02-( log(readval/3960.0) )/30.0 for
        readval in self.robot.read_proximity_sensors() ]
