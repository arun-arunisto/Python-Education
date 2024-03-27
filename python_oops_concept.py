"""
class : class is a blueprint for creating objects.
        it defines the attributes (data) and methods
        (function) that the objects will have
object: object is an instance of a class
"""
#sample
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving")

#creating objects of the class
car_1 = Car("Toyota", "Corolla")
car_2 = Car("Tesla", "Model S")

#calling methods on object
car_1.drive()
car_2.drive()

"""
Inheritance
Inheritance allows a class(sub class) to inherit
attributes and methods from another class (super class)
"""
class Employee_details:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def emp_details(self):
        print("Employee name:",self.name)
        print("Employee age:",self.age)

class Employee_designation(Employee_details):
    def __init__(self, name, age, designation, salary):
        Employee_details.__init__(self, name, age)
        self.designation = designation
        self.salary = salary

    def emp_details_with_designation(self):
        print("Employee name:",self.name)
        print("Employee age:",self.age)
        print("Employee designation:",self.designation)
        print("Employee salary:",self.salary)

#calling subclass on object
emp_1 = Employee_designation("Arunisto", 25, "Developer", "$60k")

#accessing child method
emp_1.emp_details_with_designation()
#accessing parent class too
emp_1.emp_details()
print(emp_1.name)

"""
Encapsulation:
Encapsulation is the bundling data and methods on that single unit class
"""
class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.__balance = balance #private variable

    def deposit_amount(self, amt):
        self.__balance+=amt

    def withdraw_amount(self, amt):
        self.__balance-=amt

    def get_balance(self):
        return self.__balance

acc_1 = BankAccount("12345", 5000)
print(acc_1.get_balance())
acc_1.deposit_amount(100)
print(acc_1.get_balance())
print(acc_1._BankAccount__balance) #accessing private variable

    
