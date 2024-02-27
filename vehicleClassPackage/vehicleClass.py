#vehicleClass.py

class Vehicle:
    '''
    Vehicle class
    This class models a vehicle on a used car lot  
    Change Order: we need to add maximum speed to the model 
    Change Order: Need a way to "read" the maximum speed from the model 
    Change Order: Some developers need to use the constructor without having to provide a max speed
    '''
    # constructor. it's called when ...  we instantiate an object of vehicle type
    def __init__(self, type, max_speed = None):
        '''
        @Param type: The kind of vehicle
        @Param max_speed: Maximum speed of the vehicle, defaults to None
        '''
        self.type = type;
        self._thisisprivate = 42 #this is a weak attempt to support data hiding
        self.max_speed = max_speed #save a copy in the current object
    #an instance method. it operates on an instance of the vehicle class   
    def printType(self):
        print(self.type);
        
    def getSpeed(self):            #this is called a getter
        return self.max_speed
    
    
if __name__ =="__main__":
    #some code to test the class would go here. 
    #if no code, just pass.
    pass

    