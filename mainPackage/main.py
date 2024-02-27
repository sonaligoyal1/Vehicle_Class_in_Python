#main.py

from vehicleClassPackage.vehicleClass import * 

if __name__=="__main__":
    #instantiate an object if type Vehicle
    myCorvette = Vehicle("Car", 120) #trigger a call to construction
    myCorvette.printType()     # invoking the method on the object
      
    #invoke the getter for maximum speed, store the return value in a variable
    #print that to the console
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed:", maximum_speed)

    #instantiate another vehicle object, I can name it
    myCorolla = Vehicle("Car")            #myCorolla is an object of type Vehicle
    
    #I want a list of three vehicles: car, boat, and spaceship
    #you can pick the names and properties
    #I want some friendly output to demo your work
    
    myVehicles = [  Vehicle("Toyota Camry", 150)
                  , Vehicle("Sailboat", 20)
                  , Vehicle("Falcon Heavy", 4000)]
    #iterate over the list
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed()) 

    
  
    
    
    