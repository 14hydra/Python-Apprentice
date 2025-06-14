class Car:
    """
    
    has 4 wheels, a color, a model, an age
    
    """
    windshieldcolor = "clear"
    def __init__(self, numwheels, color, model):
        self.numwheels = numwheels
        self.color = color
        self.model = model

        self.mileage = 0

    def drive(self, hoursdriven, speed):
        self.mileage = self.mileage + hoursdriven * speed


    def __str__(self):
        return "Car with " + str(self.numwheels) + " wheels, a color of " + str(self.color) + ", and a model of " + str(self.model) + ", with a " + Car.windshieldcolor + " windshield and a mileage of " + str(self.mileage)



if __name__ == "__main__":
    car1 = Car(4, "green", "tesla")
    car2 = Car(4, "black", "dodge")
    car3 = Car(numwheels=4, model="corvette", color="grey")

    car1.drive(1, 60)
    car2.drive(2, 40)
    car3.drive(3, 80)

    print(str(car1) + "\n" + str(car2) + "\n" + str(car3))