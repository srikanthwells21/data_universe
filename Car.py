class Car:
    max_speed = 200

    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed

    def acceelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += Car.max_speed
        else:
            self.speed = Car.max_speed

    def get_speed(self):
        return self.speed

car1 = Car("Toyota","Camry","Blue")
car2 = Car("Honda","Civic","Red")
    
car1.acceelerate(30)
car2.acceelerate(10)

print(f"{car1.make} {car1.model} {car1.color} is currently at {car1.get_speed()} km/h. ")

print(f"{car2.make} {car2.model} {car2.color} is currently at {car2.get_speed()} km/h. ")