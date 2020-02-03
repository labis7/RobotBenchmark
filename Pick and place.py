"""Sample Webots controller for the pick and place benchmark."""

from controller import Robot

# Create the Robot instance.
robot = Robot()

# Get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Inizialize base motors.
wheels = []
wheels.append(robot.getMotor("wheel1"))
wheels.append(robot.getMotor("wheel2"))
wheels.append(robot.getMotor("wheel3"))
wheels.append(robot.getMotor("wheel4"))
for wheel in wheels:
    # Activate controlling the motors setting the velocity.
    # Otherwise by default the motor expects to be controlled in force or position,
    # and setVelocity will set the maximum motor velocity instead of the target velocity.
    wheel.setPosition(float('+inf')) 

# Initialize arm motors.
armMotors = []
armMotors.append(robot.getMotor("arm1"))
armMotors.append(robot.getMotor("arm2"))
armMotors.append(robot.getMotor("arm3"))
armMotors.append(robot.getMotor("arm4"))
armMotors.append(robot.getMotor("arm5"))
# Set the maximum motor velocity.




armMotors[0].setVelocity(1.57) # max 1.57
armMotors[1].setVelocity(1.57) #max 1.57
armMotors[2].setVelocity(1.57)
armMotors[3].setVelocity(1.57)

# Initialize arm position sensors.
# These sensors can be used to get the current joint position and monitor the joint movements.
armPositionSensors = []
armPositionSensors.append(robot.getPositionSensor("arm1sensor"))
armPositionSensors.append(robot.getPositionSensor("arm2sensor"))
armPositionSensors.append(robot.getPositionSensor("arm3sensor"))
armPositionSensors.append(robot.getPositionSensor("arm4sensor"))
armPositionSensors.append(robot.getPositionSensor("arm5sensor"))
for sensor in armPositionSensors:
    sensor.enable(timestep)

# Initialize gripper motors.
finger1 = robot.getMotor("finger1")
finger2 = robot.getMotor("finger2")
# Set the maximum motor velocity.
finger1.setVelocity(10)
finger2.setVelocity(10)
# Read the miminum and maximum position of the gripper motors.
fingerMinPosition = finger1.getMinPosition()
fingerMaxPosition = finger1.getMaxPosition()



# Move forward. 14.81 is the max velocity of the wheels
for wheel in wheels:
    wheel.setVelocity(14.81)
# Wait until the robot is in front of the box.
# Move arm and open gripper.
#armMotors[0].setPosition(-0.05)
armMotors[1].setPosition(-1.13)
armMotors[2].setPosition(-0.35)
armMotors[3].setPosition(-0.5)
finger1.setPosition(fingerMaxPosition)
finger2.setPosition(fingerMaxPosition)

# Monitor the arm joint position to detect when the motion is completed.
#while robot.step(timestep) != -1:
#    if abs(armPositionSensors[3].getValue() - (-1.2)) < 0.01:
        # Motion completed.
#        break
robot.step(235 * timestep)
armMotors[3].setPosition(-0.7)
for wheel in wheels:
    wheel.setVelocity(0.0)
robot.step(18 * timestep)





# Close gripper.
finger1.setPosition(0.013)
finger2.setPosition(0.013)
# Wait until the gripper is closed.
robot.step(11 * timestep) 
for wheel in wheels:
    wheel.setVelocity(-14.81)
armMotors[2].setPosition(-0.2)

#robot.step(1 * timestep) 
################################## ARM INVERT
# Lift arm.
armMotors[0].setPosition(0.2)
armMotors[1].setPosition(-0.7)
armMotors[2].setPosition(-0.2)
armMotors[3].setPosition(-1)
# Wait until the arm is lifted.
###################################
#robot.step(5 * timestep)


robot.step(100 * timestep)
armMotors[0].setPosition(2.65)
armMotors[1].setPosition(-0.5)
armMotors[2].setPosition(0)
armMotors[3].setPosition(0)
robot.step(102 * timestep)
armMotors[1].setPosition(-1.13)
robot.step(10 * timestep)
finger1.setPosition(fingerMaxPosition)
finger2.setPosition(fingerMaxPosition)
robot.step(50 * timestep)
for wheel in wheels:
    wheel.setVelocity(0.0)
