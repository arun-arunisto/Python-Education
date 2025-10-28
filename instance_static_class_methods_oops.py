# instance methods
class Sample:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"My name is :{self.name}"

obj = Sample("Arun")
print(obj.greet()) # My name is Arun


# class method
class Sample:
    name = "Arun"

    @classmethod
    def change_name(cls, name):
        cls.name = name

print(Sample.name) # Arun
Sample.change_name("Arun Arunisto")
print(Sample.name) #Arunisto

# factory method
class Sample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, 2025-year)

obj1 = Sample("Arun", 1996)
print(obj1.name) # Arun
print(obj1.age) # 1996
obj2 = Sample.from_birth_year("Arun", 1996)
print(obj2.name) # Arun
print(obj2.age) #29


# static method
class Sample:
    @staticmethod
    def add(a, b):
        return a+b

print(Sample.add(20, 30))




