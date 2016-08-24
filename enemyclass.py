"""
#Classes basics
class Enemy:
    # class varibale
    life = 3 
    
    def attack(self):
        print " death"
        self.life -= 1 
    
    def checklife(self):
        if self.life <= 0 :
            print "die"
        else:
            print(str(self.life) + " life  left")
            
            
enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
#enemy2.attack()

enemy1.checklife()
enemy2.checklife()

"""
"""
# def __init__

class Enemy:
    def __init__(self,x):
        self.energy = x
        
    def get_energy(self):
        print(self.energy)
        
        
ravi = Enemy(10)
kavi = Enemy(20)

ravi.get_energy()
#kavi.get_energy()


"""

"""

class Add:
    def __init__(self,x,y):
        self.run = x
        self.fun = y
        
    def plus(self):
        c = self.run + self.fun 
        print c
        
    def mul(self):
        c = self.run *  self.fun 
        print c
    def sub(self):
        c = self.run - self.fun 
        print c
    def div(self):
        c = self.run / self.fun 
        print c
        
        
tap = Add(50,30)
gap = Add(40,35)


tap.plus()
gap.plus()

tap.mul()
gap.mul()

tap.sub()
gap.sub()

tap.div()
gap.div()

"""
"""
#class variable vs instance variable
class Girl:
    gender = " female"
    
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height= height
        self.weight = weight 
        
r = Girl('helo',25,170,61)
p = Girl('celo',28,171,61)
print(r.gender)
print(p.gender)

print(r.name)
print(p.name)

print(r.age)
print(p.age)

print(r.height)
print(p.height)

print(r.weight)
print(p.weight)


"""

"""
#inheritance
class Parent():

    def last_name(self):
        print "alluri"
        
        
class Child(Parent):


    def first_name(self):
        print " ravi"
        
       
     #child class can overriding parent class as below. 
    def last_name(self):
        print "Anthony"
        
        
kavi = Child()
kavi.last_name()
kavi.first_name()


"""
#Multiple Inheritance
"""
class Mario():
    def move(self):
        print " moved toward right"


    def jump(self):
        print " jump up"
        
class Shroom():
    def food(self):
        print " grow up"
        
        
class Flag(Mario,Shroom):
       # pass is used when you are mention nothing in the class
    pass
            

dheeru = Flag()

dheeru.move()
dheeru.jump()
dheeru.food()

"""

"""
#multithreading

import threading

class Messenger(threading.Thread):
    def run(slef):
        for i in range(10):
            print(threading.currentThread().getName())
            
            
x = Messenger(name="send message")
y = Messenger(name="receive Messenger")
x.start()
y.start()

"""










