 # -*- coding: utf-8 -*-

#Наследование продолжаем изучать

# Создаём класс Figure базовый класс

class Figure:
    def __init__(self, side = 0.0):
        self.side = side

# Создаём дочерний класс Square от родительского класса Figure

class Square(Figure):
    def Draw(self):
        for i in range(self.side):
            print('* ' * self.side)

# Ещё один класс, который будет наследоваться от класса Figure

class Triangle(Figure):
    def Draw(self):
        for i in range(1, self.side + 1):
            print('* ' * i)


# А теперь создаём объекты самих классов

def main():
    square = Square(8)
    triangle = Triangle(8)

    # И на обоих их вызовем метод Draw
    square.Draw()
    print()
    triangle.Draw()
    

if __name__ == '__main__':
    main() 