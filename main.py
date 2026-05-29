

# 1
class Car:
    def drive(self):
        return "Car is driving"

# 2
class Student:
    def __init__(self, name):
        self.name = name

# 3
class Animal:
    def sound(self):
        return "Animal sound"

# 4
class Dog(Animal):
    def sound(self):
        return "Woof"

# 5
class Cat(Animal):
    def sound(self):
        return "Meow"

# 6
class Book:
    def __init__(self, title):
        self.title = title

# 7
class Phone:
    brand = "Samsung"

# 8
class Teacher:
    def teach(self):
        return "Teaching..."

# 9
class Laptop:
    def __init__(self, model):
        self.model = model

# 10
class Person:
    def __init__(self, age):
        self.age = age
