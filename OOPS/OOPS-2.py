# INHERITANCE

class Vehicle:
    def __init__(self,color,maxSpeed):
        self.color = color
        self.maxSpeed = maxSpeed

    def print(self):
        print("Color :", self.color)
        print("Max Speed :", self.maxSpeed)
        print(c.color,end="")

class Car(Vehicle):                                                         #to inherit properties from a class add the name of upper class in the other class
    def __init__(self, color, maxSpeed, numGears, isConvertible):
        super().__init__(color, maxSpeed)                                   # this helps in initializing the inherited properties from the inherited class
        self.numGears = numGears
        self.isConvertible = isConvertible

    def printCar(self):
        self.print()                                                        #using this way enables us to print the private variables of the parent class
        print("Number Of Gears :", self.numGears)
        print("Is it Convertible? ", self.isConvertible)


c1 = Car("red", 250, 6, "No")
c1.printCar()

#---------------------------------------------

class Circle(object):                                                       # same as "class Circle:"
    def __init__(self,radius):
        self.radius = radius

    def __str__(self) -> str:
        return "This is a Circle Class which takes radius as an argument"
    
c = Circle(3)
print(c)

#---------------------------------------------

#Multiple Inheritance

class Mother:
    def print(self):
        print ("Mother")
    
class Father:                                       # Since print is a function in both the base classes if the print function is called by the derived class
    def print(self):                                #, print function of the class written first in the bracket of the derived class will be used
        print("father")
    
class Child(Father, Mother):
    def printChild(self):
        print ("Child")
    
c = Child()
print(Child.mro())                                  #to see the order in which the initailization will happen
c.print()

#---------------------------------------------

#Operator Overloading

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,otherPoint):
        return (self.x+otherPoint.x, self.y+otherPoint.y)
    
    def __lt__(self,otherPoint):                                #less than function compared using the hypotenuse 
        return (math.sqrt(self.__x**2 + self.__y**2) < math.sqrt(point_object.__x**2 + point_object.__y**2))
    
p1 = Point(1,2)
p2 = Point(4,5)

print(p1+p2)
