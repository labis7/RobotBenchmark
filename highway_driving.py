"""Sample Webots controller for highway driving benchmark."""

from vehicle import Driver

# name of the available distance sensors
sensorsNames = [
    'front',
    'front right 0',
    'front right 1',
    'front right 2',
    'front left 0',
    'front left 1',
    'front left 2',
    'rear',
    'rear left',
    'rear right',
    'right',
    'left']
sensors = {}

maxSpeed = 100
driver = Driver()
driver.setSteeringAngle(0.0)  # go straight



# get and enable the distance sensors
for name in sensorsNames:
    sensors[name] = driver.getDistanceSensor('distance sensor ' + name)
    sensors[name].enable(10)

# get and enable the GPS
gps = driver.getGPS('gps')
gps.enable(10)

# get the camera
camera = driver.getCamera('camera')
# uncomment those lines to enable the camera
#camera.enable(50)
#camera.recognitionEnable(50)
dest =0
prevpos = -2
counter=0
while driver.step() != -1:
    # adjust the speed according to the value returned by the front distance sensor
    frontDistance = sensors['front'].getValue()
    frontRange = sensors['front'].getMaxValue()
    speed = maxSpeed * frontDistance / frontRange
    driver.setCruisingSpeed(speed)
    # brake if we need to reduce the speed
    speedDiff = driver.getCurrentSpeed() - speed
    x=gps.getValues()
    
    if(dest == 2):#1.3
        #if(x[0]<1.3): #then turn left
        driver.setSteeringAngle(60*(x[0] - prevpos)*0.05 + (x[0]-1.3)*0.04) #TUNNING!!
        #if(x[0]>1.3): #then turn right
        #    driver.setSteeringAngle(1*0.1)

        #continue
    if(dest == 1):# 5.2
       #if(x[0]<1.3): #then turn left
       driver.setSteeringAngle(60*(x[0] - prevpos)*0.05 + (x[0]-5.2)*0.04)
       #if(x[0]>1.3): #then turn right
       #    driver.setSteeringAngle(1*0.1)
 
       #continue   
    if(dest == 3):# -2
       #if(x[0]<1.3): #then turn left
       driver.setSteeringAngle(60*(x[0] - prevpos)*0.05 + (x[0]+2)*0.04)
       #if(x[0]>1.3): #then turn right
       #    driver.setSteeringAngle(1*0.1)
       prevpos = x[0]
       #continue    
    prevpos = x[0] 
    counter=counter +1
    if ((speedDiff > 0)):
        print(counter)
        if((sensors['right'].getValue()>3)and(sensors['front right 2'].getValue()>8)and(not(sensors['right'].getValue()<7))): #you can turn right
             print("trying right")
             if((x[0]<5.25)and(x[0]>5.15)): #means you are left, go middle
                 dest = 2 #middle
             if((x[0]<1.5)and(x[0]>1)):  #1.3, you are middle,go right
                 dest = 3 #right
        elif((sensors['left'].getValue()>3)and(sensors['front left 2'].getValue()>8)and(sensors['front left 1'].getValue()>14)): #You can steer left  
            #driver.setSteeringAngle(-speedDiff*0.1)
            print("trying left")
            if((x[0]<-1.5)and(x[0]>-2.5)): #-2, you are in the right row, go left
                dest = 2 #middle
            if((x[0]<1.5)and(x[0]>1)):  #1.3, you are middle,go left
                dest = 1 #left
        else:    
            driver.setBrakeIntensity(100)
    else:
        driver.setBrakeIntensity(0)
        maxSpeed = 120
        
   

        
        
