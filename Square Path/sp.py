"""Sample Webots controller for the square path benchmark."""

from controller import Robot

# Get pointer to the robot.
robot = Robot()

# Get pointer to each wheel of our robot.
leftWheel = robot.getMotor('left wheel')
rightWheel = robot.getMotor('right wheel')

rightWheelSensor = robot.getPositionSensor('right wheel sensor')
rightWheelSensor.enable(1) # Refreshes the sensor every 16ms.
res = rightWheelSensor.getValue()


#maxvelocity = 5.24
# Repeat the following 4 times (once for each side).
for i in range(0, 4):
    if(i == 0):
        # First set both wheels to go forward, so the robot goes straight.
        leftWheel.setPosition(1000)
        rightWheel.setPosition(1000)
        # Wait for the robot to reach a corner.
        #robot.step(3905)
        #leftWheel.setVelocity(5.23)
        #res = round(rightWheelSensor.getValue(),1)
        res=0
        while( res <= 20.42):
            robot.step(1)
            res = round(rightWheelSensor.getValue(),3)
            
        # Then, set the right wheel backward, so the robot will turn right.
        leftWheel.setPosition(1000)
        rightWheel.setPosition(-1000)
        #rightWheel.setVelocity(5.22)
        # Wait until the robot has turned 90 degrees clockwise.
        #robot.step(464)
        while(res>= 18.08):
            robot.step(1)
            res = round(rightWheelSensor.getValue(),3)
        #print(res)
        
    if(i == 1):
        # First set both wheels to go forward, so the robot goes straight.
        leftWheel.setPosition(1000)
        rightWheel.setPosition(1000)
        rightWheel.setVelocity(5.19)
        res = round(rightWheelSensor.getValue(),3)
        while( res <= 38.75):
            robot.step(1)
            res = round(rightWheelSensor.getValue(),3)
        print(res)
        # Then, set the right wheel backward, so the robot will turn right.
        leftWheel.setPosition(1000)
        rightWheel.setPosition(-1000)
        
        while(res >= 36.48):
            robot.step(1)
            res = round(rightWheelSensor.getValue(),3)

    if(i == 2):
        # First set both wheels to go forward, so the robot goes straight.
        leftWheel.setPosition(1000)
        rightWheel.setPosition(1000)
        leftWheel.setVelocity(5.19)
        res = round(rightWheelSensor.getValue(),1)
        while( res != 57.2):
            robot.step(1)
            res = round(rightWheelSensor.getValue(),1)
        #print(res)
        # Then, set the right wheel backward, so the robot will turn right.
        leftWheel.setPosition(1000)
        rightWheel.setPosition(-1000)
        
        while(res >= 54.81):
            robot.step(1)
            res = round(rightWheelSensor.getValue(),3)
    
    
    if(i == 3):
        # First set both wheels to go forward, so the robot goes straight.
        leftWheel.setPosition(1000)
        rightWheel.setPosition(1000)
        rightWheel.setVelocity(5.20)
        res = round(rightWheelSensor.getValue(),1)
        while( res != 75.5):
            robot.step(1)
            res = round(rightWheelSensor.getValue(),1)
        #print(res)
        # Then, set the right wheel backward, so the robot will turn right.
        leftWheel.setPosition(1000)
        rightWheel.setPosition(-1000)
        
        while(res >= 75.11):
            robot.step(1)
            res = round(rightWheelSensor.getValue(),3)
    #res = rightWheelSensor.getValue()
    #print(res)
    
    

# Stop the robot when path is completed, as the robot performance
# is only computed when the robot has stopped.
leftWheel.setVelocity(0)
rightWheel.setVelocity(0)
