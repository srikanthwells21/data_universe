class Circle(object):
    #constructor
    def __init__(self, radius=3, color="White"):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius

c1 = Circle(4, "Blue") 
print(f"Circle radius is {c1.radius} and color is {c1.color}.")

