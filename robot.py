class Robot:
    """Represent a robot , with a name . """
    population = 0
    
    
    def __init__(self,name):
        self.name = name
        print("(Intializing {} )".format(self.name))
        
        
        Robot.population += 1
        
    def die(self):
        """ I am dying."""
        print ("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print ("{}was the last one.".format(self.name))
        else:
            print ("there are still{:d} robots working.".format(Robot.population))
            
            
            
            
    def say_hi(self):
        """ Greeting by the robot yeah they can do that."""
        print ("Greeting, my master call me {} . " .format(self.name))
        
        
    def how_many(cls):
        print ("we have {:d} robots." ,format(cls.population))
              
               
        
droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()


droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\n Robots Can do somework here.\n")
print ("Robot have finished thier work .so lets destroy them.")

droid1.die()
droid2.die()
Robot.how_many()




