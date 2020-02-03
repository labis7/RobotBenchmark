"""Sample Webots controller for the inverted pendulum benchmark."""

from controller import Robot
import math

# Get pointer to the robot.
robot = Robot()

# Get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Get pointers to the position sensor and enable it.
ps = robot.getPositionSensor('pendulum sensor')
ps.enable(timestep)

# Get pointers to the motors and set target position to infinity (speed control).
leftMotor = robot.getMotor("left wheel motor")
rightMotor = robot.getMotor("right wheel motor")
leftMotor.setPosition(float('+inf'))
rightMotor.setPosition(float('+inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)
maxSpeed = min(rightMotor.getMaxVelocity(), leftMotor.getMaxVelocity())

# Define the PID control constants and variables.
KP = 120  #120
KI = 93   #95  #100 #80 
KD = 0    #0
integral = 0.0
previous_position = 0.0

# Initialize the robot speed (left wheel, right wheel).
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)
counter =0
# Main loop: perform a simulation step until the simulation is over.
while robot.step(timestep) != -1:
    # Read the sensor measurement.
    position = ps.getValue()
    
    if(counter == 500):
        counter=501
    else:
        counter = counter +1
    
    if(counter ==12500): #51- 52 = 13000
        print("\n\n\n1st Change!\n\n\n")
        KP = 120
        KI =110
        #KD=50
    if(counter ==13000): #51- 52 = 13000
        print("\n\n\n2nd Change!\n\n\n")
        #### 53 seconds mark until ~1 min ####
        KP = 135
        KI = 115 #from before
        #KD = 30   
        #########################
              
    # Stop the robot when the pendulum falls.
    if math.fabs(position) > math.pi * 0.5:
        leftMotor.setVelocity(0.0)
        rightMotor.setVelocity(0.0)
        time = robot.getTime()
        print("Time:%-24.3f" % time)
        break

    # PID control.
    integral = integral + (position + previous_position) * 0.5 / timestep
    derivative = (position - previous_position) / timestep
    speed = KP * position + KI * integral + KD * derivative


    #if(((position > 0.022)or(position <-0.022))and(counter > 500)):
    #    print(position)

        #KI =180
        #KD = 50
        #KP = 300
     
        
    # Clamp speed to the maximum speed.
    if speed > maxSpeed:
        speed = maxSpeed
    elif speed < -maxSpeed:
        speed = -maxSpeed

    # Set the robot speed (left wheel, right wheel).
    leftMotor.setVelocity(-speed)
    rightMotor.setVelocity(-speed)

    # Store previous position for the next controller step.
    previous_position = position
