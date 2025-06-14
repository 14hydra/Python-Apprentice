class Car:
    """
    
    has 4 wheels, a color, a model, an age
    
    """

    def __init__(self, numwheels, color, model):
        self.numwheels = numwheels
        self.color = color
        self.model = model


    def __str__(self):
        return "Car with " + str(self.numwheels) + " wheels, a color of " + str(self.color) + ", and a model of " + str(self.model)
    
class Motorcycle(Car):

    """
    has 2 wheels, a color, a model
    """

    def __init__(self, color, model):
        Car.__init__(self, 2, color, model)


if __name__ == "__main__":
    car1 = Car(4, "green", "tesla")
    car2 = Car(4, "black", "dodge")
    car3 = Car(numwheels=4, model="corvette", color="grey")

    print(str(car1) + "\n" + str(car2) + "\n" + str(car3))