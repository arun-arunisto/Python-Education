# class without dataclass
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Name:{self.name}, Age:{self.age}"

per1 = Person("Arun", 28)
print(per1) #Name:Arun, Age:28
"""
#class with dataclass
"""
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

per1 = Person("Arun", 28)
print(per1) #Person(name='Arun', age=28)
"""
# default values and immutability
"""
from dataclasses import dataclass

@dataclass(frozen=True) #makes immutable
class Product:
    name: str
    price: float = 0.0 #default value
    in_stock: bool = True #default

item = Product("Phone", 999)
print(item) #Product(name='Phone', price=999, in_stock=True)
# This will raise an error because frozen=True makes it immutable
item.price = 1000 #FrozenInstanceError
"""
# class with custom methods
"""
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    emp_id: int
    salary: float

    def give_raise(self, percentage):
        self.salary+=self.salary*(percentage/100)

emp = Employee("Arun", 101, 50000)
print(emp) #Employee(name='Arun', emp_id=101, salary=50000)
emp.give_raise(10)
print(emp) #Employee(name='Arun', emp_id=101, salary=55000.0)
"""
# nested dataclasses
"""
from dataclasses import dataclass

@dataclass
class Company:
    reg_name: str
    city: str

@dataclass
class Employee:
    name: str
    role: str
    company: Company

com = Company("RB", "BNG")
emp = Employee("Arun", "dev", com)
print(emp)
#Employee(name='Arun', role='dev', company=Company(reg_name='RB', city='BNG'))
"""
# ordering and comparison
"""
from dataclasses import dataclass

@dataclass(order=True)
class Employee:
    name: str
    salary: int

emp1 = Employee("Arunisto", 5000)
emp2 = Employee("Arun", 1000)

print(emp2 > emp1)
#False (Compares attributes in order: name, salary)
print(sorted([emp1, emp2]))
"""
"""
result:
[Employee(name='Arun', salary=1000), Employee(name='Arunisto', salary=5000)]
"""
# post-initialization with __post_init__
"""
from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int
    area: int = 0 # will be compute

    def __post_init__(self):
        self.area = self.width*self.height

rect = Rectangle(40, 50)
print(rect) #Rectangle(width=40, height=50, area=2000)
"""
# inheritance with dataclass
from dataclasses import dataclass

@dataclass
class Vehicle:
    make: str
    year: int

@dataclass
class Car(Vehicle):
    model: str
    doors: int = 4

car = Car(make="Toyota", year=2020, model="Camry")
print(car)
#Car(make='Toyota', year=2020, model='Camry', doors=4)
