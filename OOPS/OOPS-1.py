class Student:
    pass

s1 = Student()

s1.name = "Vasu"                                            #adding attributes in the class externally
s1.rollNumber = 139

print(s1.__dict__)                                          #printing key value pairs

print(hasattr(s1,"name"))                                   #checking whether "s1" has an attribute of "name"

#---------------------------------------------

class Student:

    passingPercentage = 40                                  #class attribute

    def studentDetails(self):
        self.name = "Vasu"                                  #instance attribute
        self.percentage = 80
        print("Name = ", self.name)
        print("Percentage = ", self.percentage)
        pass

    def isPassed(self):
        if self.percentage>= self.passingPercentage:
            print("pass")
        else:
            print("Fail")
        pass

    @staticmethod                                           #static method(function)- by default self passed in the functons is ignored
    def welcomeToSchool():
        print("Hey, Welcome to school!!")

s1 =Student()                                               #creating an object
s1.studentDetails()                                         #using the function in the class to add the instance attributes
s1.isPassed()
s1.welcomeToSchool()

#---------------------------------------------

class Student:
    def __init__(self, name, rollNumber):                  #__init__ function doesn't have to be called
        self.name = name
        self.rollNumber = rollNumber
        pass

    @staticmethod                                         
    def welcome():
        print("Welcome!!")

s1 = Student("Vasu", 20)

#---------------------------------------------

from datetime import date

class Student:                                                  #do not run the code as the function in class method has object created with enteries of name age                                                                  and percentage but we dont ahve any class with these enteries
    def __init__(self, name, rollNumber):                 
        self.name = name
        self.rollNumber = rollNumber
        pass

    @classmethod                                                #used to create a function which returns an object in the specified class using the specific                                                                      entries required
    def fromBirthYear(cls, name, year, percentage):
        return cls(name, date.today().year-year,percentage)

#---------------------------------------------

class Fraction:                                                  #class of fraction numbers with some functions
    def __init__(self, num = 0, den = 1):
        self.num = num
        self.den = den
    
    def print(self):
        if self.num==0:
            print (0)
        elif self.den==1:
            print(self.num)
        else:
            print(self.num, "/", self.den)

    def simplify(self):
        if self.num==0:
            self.den=1
            return
        current = min(self.den,self.num)
        while current>1:
            if self.num%current == 0 and self.den%current == 0:
                break
            current = current -1
        self.den = self.den//current
        self.num = self.num//current

    def add(self,otherFraction):
        newNum = (otherFraction.den*self.num)+(otherFraction.num*self.den)
        newDen = (otherFraction.den*self.den)

        self.num = newNum
        self.den = newDen
        self.simplify()

    def multiply(self,otherFraction):
        newNum = otherFraction.num*self.num
        newDen = otherFraction.den*self.den

        self.num = newNum
        self.den = newDen
        self.simplify()

f1 = Fraction(2,5)
f2 = Fraction(3,2)

f1.multiply(f2)

f1.print()

#---------------------------------------------

class Complex:                                                       #complex number class
    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img
        
    def print(self):
        if self.real == 0 and self.img == 0:
            return(0)
        elif self.real ==0 and self.img!=0:
            print(self.img,"i")
        elif self.real!=0 and self.img==0:
            print(self.real)
        else:
            print(self.real, "+", self.img, "i")

    def add(self, otherComplex):
        newReal = self.real + otherComplex.real
        newImg = self.img + otherComplex.img

        self.real = newReal
        self.img = newImg
        self.print()

    def multiply(self,otherComplex):
        newReal = (self.real*otherComplex.real)-(self.img*otherComplex.img)
        newImg = (self.real*otherComplex.img)+(self.img*otherComplex.real)

        self.real = newReal
        self.img = newImg
        self.print()

c1 = Complex(5,2)
c2 = Complex(3,5)

c1.multiply(c2)
