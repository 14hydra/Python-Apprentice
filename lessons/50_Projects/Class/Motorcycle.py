from Car import Car

class Motorcycle(Car):

    """
    has 2 wheels, a color, a model
    """

    def __init__(self, color, model):
        Car.__init__(self, 2, color, model)