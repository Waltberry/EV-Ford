from pid import PID

# Initialize the PID controller with appropriate gains
pid_controller = PID(p=0.2, i=0.02, d=0.1)

# Setpoint is the desired velocity
setpoint_velocity = 10

# Current velocity feedback from the robot
current_velocity = 8

# Calculate the control output
control_output = pid_controller.update(setpoint_velocity, current_velocity)

print("Control output:", control_output)
