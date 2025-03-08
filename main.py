import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return ((self.a + self.b) / 2) * math.sqrt((self.c - self.d) ** 2)


class Parallelogram:
    def __init__(self, a, b, height):
        self.a = a
        self.b = b
        self.height = height

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


def read_input(file_path):
    shapes = []
    with open(file_path, 'r') as f:
        for line in f:
            data = line.strip().split()
            shape_type = data[0]
            params = list(map(float, data[1:]))

            if shape_type == "Triangle":
                shapes.append(Triangle(*params))
            elif shape_type == "Rectangle":
                shapes.append(Rectangle(*params))
            elif shape_type == "Trapeze":
                shapes.append(Trapeze(*params))
            elif shape_type == "Parallelogram":
                shapes.append(Parallelogram(*params))
            elif shape_type == "Circle":
                shapes.append(Circle(*params))

    return shapes


def find_max_area_and_perimeter(shapes):
    max_area = 0
    max_perimeter = 0
    max_shape_area = None
    max_shape_perimeter = None

    for shape in shapes:
        area = shape.area()
        perimeter = shape.perimeter()

        if area > max_area:
            max_area = area
            max_shape_area = shape

        if perimeter > max_perimeter:
            max_perimeter = perimeter
            max_shape_perimeter = shape

    return max_shape_area, max_shape_perimeter


shapes = read_input('input01.txt')
max_shape_area, max_shape_perimeter = find_max_area_and_perimeter(shapes)

print(f"Shape with max area: {max_shape_area.__class__.__name__}, Area: {max_shape_area.area()}, Perimeter: {max_shape_area.perimeter()}")
print(f"Shape with max perimeter: {max_shape_perimeter.__class__.__name__}, Area: {max_shape_perimeter.area()}, Perimeter: {max_shape_perimeter.perimeter()}")

