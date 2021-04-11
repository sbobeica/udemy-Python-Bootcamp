class Cylinder:

    pi = 3.14

    def __init__(self, height = 1, radius = 1):

        self.radius = radius
        self.height = height

    def volume(self):
        return  self.pi * self.height * (self.radius) ** 2

    def surface_area(self):
        top = 2 * self.pi *self.radius**2
        return top + 2*self.pi*self.radius*self.height

cylinder = Cylinder(2,3)
print(cylinder.volume())
print(cylinder.surface_area())


class Line:

    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        [x1, y1] = self.coord1
        [x2, y2] = self.coord2
        # (x1, y1) = self.coord1
        # (x2, y2) = self.coord2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        [x1, y1] = self.coord1
        [x2, y2] = self.coord2
        # (x1, y1) = self.coord1
        # (x2, y2) = self.coord2
        return (y2 - y1)/(x2 - x1)


coordinate1 = [3, 2]
coordinate2 = [8, 10]

# line = Line((3, 2), (8, 10))
ls = Line(coordinate1, coordinate2)

print(ls.distance())
print(ls.slope())
# print(line.distance())
# print(line.slope())

