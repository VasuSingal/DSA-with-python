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
