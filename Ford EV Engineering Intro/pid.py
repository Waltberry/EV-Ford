class PID:
    def __init__(self, p, i, d):
        self.kp = p
        self.ki = i
        self.kd = d
        self.prev_error = 0
        self.integral = 0

    def update(self, setpoint, measured_value):
        error = setpoint - measured_value
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative

# Example of PID controller usage
pid = PID(1.0, 0.1, 0.01)

setpoint = 100  # Target value
measured_value = 90  # Current value

control = pid.update(setpoint, measured_value)
print("Control output:", control)
