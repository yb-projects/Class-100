import time
class Car(object):
    def __init__(self, model, company, color, speed_limit, car_type, speed, gear, fuel):
        self.model = model
        self.company = company
        self.color = color
        self.speed_limit = speed_limit
        self.car_type = car_type
        self.speed = speed
        self.gear = gear
        self.fuel = fuel

    def start(self, boolean):
        if boolean:
            print("Started the car. Have a nice journey! :)")
        else:
            print("Engine is off.")

    def accelerate(self, speed):
        print(f"Accelerating the car to {speed} km/h. Fuel is {self.fuel}")
        self.speed = speed

        self.fuel -= speed/10

        if(self.fuel <= 10):
            print(f"Low fuel. Fuel is {self.fuel}")
        elif (self.fuel == 0):
            print("Engine off.")

    def changeGear(self, gearType):
        self.gear = gearType
        print("Gear has been changed.")

    def fillFuel(self, newLevel):
        if (newLevel <= 100):
            self.fuel = newLevel
            print(f"New fuel level: {newLevel}")
        else:
            print("Capacity exceeded.")

myCar = Car("X", "Lamborghini", "yellow", 300, "Self-Driving", 0, 1, 100)
myCar.start(True)

for i in range(15):
    myCar.accelerate(100)
    time.sleep(1)

    if(myCar.fuel == 0):
        myCar.fillFuel(100)
        #e + 38 = 10^38