"""Braitenberg-based obstacle-avoiding robot controller."""

from controller import Robot





# Get reference to the robot.
robot = Robot()

# Get simulation step length.
timeStep = int(robot.getBasicTimeStep())

# import Compass module
from controller import Compass
# get robot's Compass device
compass = robot.getCompass("compass")
# enable the Compass
compass.enable(timeStep)

# to read values
values = compass.getValues()


# Constants of the Thymio II motors and distance sensors.
maxMotorVelocity = 9.53
distanceSensorCalibrationConstant = 360

# Get left and right wheel motors.
leftMotor = robot.getMotor("motor.left")
rightMotor = robot.getMotor("motor.right")

# Get frontal distance sensors.
outerLeftSensor = robot.getDistanceSensor("prox.horizontal.0")
centralLeftSensor = robot.getDistanceSensor("prox.horizontal.1")
centralSensor = robot.getDistanceSensor("prox.horizontal.2")
centralRightSensor = robot.getDistanceSensor("prox.horizontal.3")
outerRightSensor = robot.getDistanceSensor("prox.horizontal.4")

# Enable distance sensors.
outerLeftSensor.enable(timeStep)
centralLeftSensor.enable(timeStep)
centralSensor.enable(timeStep)
centralRightSensor.enable(timeStep)
outerRightSensor.enable(timeStep)

# Disable motor PID control mode.
leftMotor.setPosition(3.5)
rightMotor.setPosition(2)

# Set ideal motor velocity.
initialVelocity = 1 * maxMotorVelocity

# Set the initial velocity of the left and right wheel motors.
leftMotor.setVelocity(initialVelocity)
rightMotor.setVelocity(initialVelocity)

start_flag = 0
counter = 0;
mult = 0
vector_mul = 1
while robot.step(timeStep) != -1:
    # Read values from four distance sensors and calibrate.
    outerLeftSensorValue = outerLeftSensor.getValue() / distanceSensorCalibrationConstant
    centralLeftSensorValue = centralLeftSensor.getValue() / distanceSensorCalibrationConstant
    centralSensorValue = centralSensor.getValue() / distanceSensorCalibrationConstant
    centralRightSensorValue = centralRightSensor.getValue() / distanceSensorCalibrationConstant
    outerRightSensorValue = outerRightSensor.getValue() / distanceSensorCalibrationConstant
    if(start_flag == 0):
        outerLeftSensorValue_old = outerLeftSensorValue
        centralLeftSensorValue_old = centralLeftSensorValue
        centralSensorValue_old = centralSensorValue
        centralRightSensorValue_old = centralRightSensorValue
        outerRightSensorValue_old = outerRightSensorValue
        start_flag=1
    
    if(counter == 43):
        leftMotor.setPosition(float('inf'))
        rightMotor.setPosition(float('inf'))
        leftMotor.setVelocity(initialVelocity)
        rightMotor.setVelocity(initialVelocity) 
        counter = 51
    else:
        counter = counter + 1
    
    if(mult != 0.1):    
        if(counter > 780):#after a certain time
            compass.enable(timeStep)
            mult = 4       #Activate compass
        if(counter >1300):
            mult = 10
        
        
    if((outerLeftSensorValue_old==outerLeftSensorValue)and(centralLeftSensorValue_old==centralLeftSensorValue)and(centralSensorValue_old==centralSensorValue)and(centralRightSensorValue_old==centralRightSensorValue)and(outerRightSensorValue_old==outerRightSensorValue)):
        if((mult == 4)or(mult == 0.1)or(mult == 10)): #IF compass activated from object or time
            initialVelocity = 1 * maxMotorVelocity
            values = compass.getValues()
            if((values[0] > 1)or(values[0]<-1)):
                mult=1
            # Set wheel velocities based on sensor values, prefer right turns if the central sensor is triggered.
            leftMotor.setVelocity(initialVelocity + values[0]*mult - (centralRightSensorValue + outerRightSensorValue) / 2)
            rightMotor.setVelocity(initialVelocity - values[0]*mult - (centralLeftSensorValue + outerLeftSensorValue) / 2 - centralSensorValue)
    else:
        initialVelocity = 0.8 * maxMotorVelocity #slow down to avoid crash
        vector_mul = 0.6
        outerLeftSensorValue_old = outerLeftSensorValue
        centralLeftSensorValue_old = centralLeftSensorValue
        centralSensorValue_old = centralSensorValue
        centralRightSensorValue_old = centralRightSensorValue
        outerRightSensorValue_old = outerRightSensorValue
        # Set wheel velocities based on sensor values, prefer right turns if the central sensor is triggered.
        leftMotor.setVelocity(initialVelocity - (centralRightSensorValue + outerRightSensorValue) / 2)
        rightMotor.setVelocity(initialVelocity - (centralLeftSensorValue + outerLeftSensorValue) / 2 - centralSensorValue)
