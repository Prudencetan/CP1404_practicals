from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # create a new Car object called "limo" that is initialized with 100 units of fuel
    limo = Car("Limo", 100)

    # print the amount of fuel in the car
    print("limo fuel = {}".format(limo.fuel))
    
    # attempt to drive the car 115km using the driving method
    limo.drive(115)
    
    # print the car's odometer reading
    print("limo's odometer now = {}".format(limo.odometer))
    print("limo fuel after driving = {}".format(limo.fuel))

    print(my_car)
    print(limo)

main()
