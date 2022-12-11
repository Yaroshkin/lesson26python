from random import randint

class Car:
    def __init__(self,name, type, kp, motor):
        self.name = name
        self.type = type
        self.kp1 = kp
        self.motor = motor
        self.numberWell = 4
        self.__vin = randint(1E4, 1E5)

    def getVin(self):
        return self.__vin

    def move(self, speed):
        print(f"move {self.name} {speed}km/h")
    
    def signal(self):
        print(f'{self.name} beep-beep')

car1 = Car("Tesla","HB", "Auto", "Electric")
car2 = Car("Porshe","Sedan", "Manual", "Dizel")

car1.move(250)
car2.signal()

print(car1.kp1)
print(car2.motor)
print(car1.getVin())

car1.kp1 = 'Manual'
car1.__vin = '111'

print(car1.kp1)
print(car2.motor)
print(car1.__vin)

#public, protected, private