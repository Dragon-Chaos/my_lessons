# -*- coding: utf-8 -*-

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def print_info(self):
        print("Name: ", self.name, "is", self.age)
        print()

#john = Person()
#john.name = "John"
#john.age = 29

#lucy = Person()
#lucy.name = "Lucy"
#lucy.age = 25

#Заменяем инициализацию вызовом
john = Person("John", 33)
lucy = Person("Lucy", 32)

print("Name: ", john.name, "is ", john.age)
print()
print("Name: ", lucy.name, "is ", lucy.age)
print()

#Обращение к функции 
Person.print_info(john)
Person.print_info(lucy)

#Обращение на прямую к методу конкретного объекта
john.print_info()
lucy.print_info()
