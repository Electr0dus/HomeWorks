class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if r >= 0 and r <= 255:
                if g >= 0 and g <= 255:
                    if b >= 0 and b <= 255:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print(f'Неверное значение для цвета')

    def __is_valid_sides(self, *args):
        for i in args:
            if isinstance(i, int) and i > 0:
                continue
            else:
                return False
        if len(args) == len(self.__sides):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    # должен возвращать периметр фигуры
    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
        else:
            return 0


class Circle(Figure):
    sides_count = 1

    def __init__(self, sides, color, filled=False):
        if isinstance(sides, list) != self.sides_count:
            sides = [1]

        super().__init__(sides, color, filled)
        c = self.get_sides()
        self.__radius = c[0] / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color, filled=False):
        if len(sides) != self.sides_count:
            sides = [1, 1, 1]
        super().__init__(sides, color, filled)
        side = self.get_sides()
        S = self.get_square()
        self.__height = (2 * S) / side[0]

    def get_square(self):
        p = super().__len__() / 2
        side = self.get_sides()
        return (p * (p - side[0]) * (p - side[1]) * (p - side[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, sides, color, filled=False):
        if isinstance(sides, list) != self.sides_count:
            sides = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        super().__init__(sides, color, filled)

    def get_volume(self):
        a = self.get_sides()
        return a[0] ** 3


circle1 = Circle(10, (200, 200, 100))
cube1 = Cube(6, (222, 35, 130))

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
