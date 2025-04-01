             # OBJECT ORIENTED PROGRAMMING #

# class Student:
#     name = 'Khirmada'

# s1 = Student()
# print(s1.name)


# class Car:
#     brand = 'Porsche'
#     color = 'Black'
#     model = '911 GT3RS'

# Car1 = Car()
# print(Car1.brand)
# print(Car1.model)



# #CONSTRUCTORS
# class Student:
#      college = "ABC College"   #CLASS ATTRIBUTE

#      def __init__(self,name,marks):   # PARAMETERIZED CONSTRUCTOR
#           self.name = name       #OBJECT ATTRIBUTE
#           self.marks = marks     #OBJECT ATTRIBUTE
#           print("Adding new student: ")

# s1 = Student('Bheem',100)
# print(s1.name,s1.marks)
# s2 = Student('Krishna',99)
# print(s2.name,s2.marks)
# print(s1.college)



# #CLASS CONSTRUCTOR AND METHOD
# class Student:

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def getavg(self):
#         sum = 0
#         for i in self.marks:
#             sum += i
#         print("Average marks of ",self.name," is: ",sum/3)

# s1 = Student('Tony Stark',[98,97,96])
# s1.getavg()



# #CLASS OF BANK ACCOUNT
# class Account:

#     def __init__(self,Acc,Bal):
#         self.account = Acc
#         self.balance = Bal

#     def debit(self,amount):
#         self.balance += amount
#         print("Rs ",amount," was debited")
#         print("Total balance: ",self.balance)

#     def credit(self,amount):
#         self.balance -= amount
#         print("Rs ",amount," was credited")
#         print("Total balance: ",self.balance)

#     def balance(self):
#         return self.balance

# Acc1 = Account(1234,50000)
# print(Acc1.account)
# print(Acc1.balance)
# Acc1.debit(10000)
# Acc1.credit(30000)



# #DELETION OF OBJECT 
# class Student:

#     def __init__(self,name):
#         self.name = name

# s1 = Student('Tony Stark')
# print(s1.name)
# del s1.name
# print(s1.name)



# #PRIVATE ATTRIBUTES AND METHODS
# class Person:
#     __name = 'Khirmada'       #PRIVATE ATTRIBUTE

#     def __hello(self):        #PRIVATE METHOD
#         print('Hello person..!!')

#     def welcome(self):
#         self.__hello()

# p1 = Person()
# print(p1.welcome())



# #INHERITANCE
# class Car:
#     @staticmethod
#     def Start():
#         print("Car started")

#     @staticmethod
#     def Stop():
#         print("Car stopped")

# class Porsche(Car):
#     def __init__(self,name):
#         self.name = name

# class Model(Porsche):
#     def __init__(self,type):
#         self.type = type
    
# car1 = Porsche("911 GT3RS")
# print(car1.name)
# print(car1.Start())
# car2 = Model("Diesel")
# print(car2.type)



# #INHERITANCE2
# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A,B):
#     varC = "Welcome t0 class C"

# C1 = C()
# print(C1.varC)
# print(C1.varA)
# print(C1.varB)



# #SUPER METHOD
# class Car:
#     def __init__(self,type):
#         self.type = type
#     @staticmethod
#     def Start():
#         print("Car started")

#     @staticmethod
#     def Stop():
#         print("Car stopped")

# class Porsche(Car):
#     def __init__(self,model,type):
#         self.model = model
#         super().__init__(type)
#         super().Start()

# car1 = Porsche('Turbo','Diesel')
# print(car1.model)
# print(car1.type)
# print(car1.Start())



# #CLASS METHOD
# class Person:
#     name = 'Khirmada'

#     # def changeName(self,name):
#     #     self.__class__.name = name

#     @classmethod
#     def changeName(cls,name):
#         cls.name = name

# p1 = Person()
# p1.changeName('Khirmada 3')
# print(p1.name)
# print(Person.name)



# #PROPERTY DECORATOR
# class Student:
#     def __init__(self,Phy,Chem,Math):
#         self.phy = Phy
#         self.chem = Chem
#         self.math = Math

#     @property
#     def Percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"
    
# s1 = Student(98,97,96)
# print(s1.Percentage)

# s1.phy = 90
# print(s1.Percentage)



# #POLYMORPHISM   DUNDER FUNCTIONS
# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img  

#     def Show(self):
#         print((self.real,"+",self.img,"i"))

#     def __add__(self,comp2):
#         newReal = self.real + comp2.real
#         newImg = self.img + comp2.img
#         return Complex(newReal,newImg)

    

# comp1 = Complex(3,2)
# comp1.Show()
# comp2 = Complex(2,4)
# comp2.Show()

# comp3 = comp1 + comp2
# comp3.Show()


#ORDER CLASS ANG __GT__ DUNDER
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,ord2):
        return self.price > ord2

ord1 = ('Chips',20)
ord2 = ('Coke',40)

print(ord1 > ord2)