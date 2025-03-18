import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.is_valid():
            raise ValueError(f"Invalid triangle sides: {a}, {b}, {c}")

    def is_valid(self):
        return (self.a + self.b > self.c and
                self.b + self.c > self.a and
                self.c + self.a > self.b)

    def area(self):
        if not self.is_valid():
            return 0
        s = (self.a + self.b + self.c) / 2
        area = s * (s - self.a) * (s - self.b) * (s - self.c)
        if area <= 0:
            return 0
        try:
            return math.sqrt(area)
        except ValueError:
            return 0

    def perimeter(self):
        return self.a + self.b + self.c


def find_max_area_and_perimeter(shapes):
    max_area = float('-inf')
    max_perimeter = float('-inf')
    max_shape_area = None
    max_shape_perimeter = None

    for shape in shapes:
        try:
            area = shape.area()
            perimeter = shape.perimeter()

            if area > max_area:
                max_area = area
                max_shape_area = shape

            if perimeter > max_perimeter:
                max_perimeter = perimeter
                max_shape_perimeter = shape
        except ValueError as e:
            print(f"Error with shape: {e}")
            continue

    return max_shape_area, max_shape_perimeter


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
            try:
                data = line.strip().split()
                shape_type = data[0]
                params = list(map(float, data[1:]))

                if shape_type == "Triangle":
                    shape = Triangle(*params)
                    if shape.is_valid():
                        shapes.append(shape)
                    else:
                        print(f"Skipping invalid Triangle: {params}")

                elif shape_type == "Rectangle":
                    if params[0] > 0 and params[1] > 0:
                        shapes.append(Rectangle(*params))
                    else:
                        print(f"Skipping invalid Rectangle: {params}")

                elif shape_type == "Trapeze":
                    if all(p > 0 for p in params):
                        shapes.append(Trapeze(*params))
                    else:
                        print(f"Skipping invalid Trapeze: {params}")

                elif shape_type == "Parallelogram":
                    if params[0] > 0 and params[1] > 0 and params[2] > 0:
                        shapes.append(Parallelogram(*params))
                    else:
                        print(f"Skipping invalid Parallelogram: {params}")

                elif shape_type == "Circle":
                    if params[0] > 0:
                        shapes.append(Circle(*params))
                    else:
                        print(f"Skipping invalid Circle: {params}")

            except (ValueError, IndexError) as e:
                print(f"Error processing line: {line.strip()} - {e}")

    return shapes


if __name__ == "__main__":
    all_shapes = []
    for file_name in ['input01.txt', 'input02.txt', 'input03.txt']:
        all_shapes.extend(read_input(file_name))

    max_shape_area, max_shape_perimeter = find_max_area_and_perimeter(all_shapes)

    try:
        if max_shape_area:
            print(f"Shape with maximum area: {max_shape_area.__class__.__name__}")
            print(f"Maximum area: {max_shape_area.area()}")
        else:
            print("No valid shape found for maximum area")

        if max_shape_perimeter:
            print(f"Shape with maximum perimeter: {max_shape_perimeter.__class__.__name__}")
            print(f"Maximum perimeter: {max_shape_perimeter.perimeter()}")
        else:
            print("No valid shape found for maximum perimeter")
    except Exception as e:
        print(f"An error occurred: {e}")