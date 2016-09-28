 # -*- coding: utf-8 -*-

#Наследование
#Создаём базовый класс

class Base:
    def metod(self):
        print("Hello")

        
#Создаём дочерний класс

class Child(Base):
    def child_metod(self):
        print("I'm happined")

#Переопределяем в дочернем классе родительский метод
    def metod(self):
        print("Hello World")

obj = Child()
obj.metod()
obj.child_metod()

