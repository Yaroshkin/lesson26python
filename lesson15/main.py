from random import randint

class Car:
    def __init__(self, name, type, kp, motor):
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
print(car1.getVin())

# public, protected, private

class Mlekopit:
    def __init__(self, age):
        self.age = age

    def eatmilk(self):
        print('ml eatmilk')
class Travoyad(Mlekopit):
    def __init__(self, age, colorGreen, n):
        super().__init__(age)
        self.colorGreen = colorGreen
        self.n = n

    def eatgreen(self):
        print("eat green")

    def eatmilk(self):
        # return super().eatmilk()
        print('tr eatmilk')
class Korova(Travoyad):
    def __init__(self, age, colorGreen, n, roga):
        super().__init__(age, colorGreen, n)
        self.roga = roga

    def eatgreen(self):
        # print("eat green")
        print('this cow')
        super().eatgreen()

    def eatmilk(self):
        # return super().eatmilk()
        print('cow eatmilk')

    def mushanie(self):
        pass

    def __str__(self):
        # return super().__str__()
        return f"Cow - {self.age} {self.colorGreen}"

class Koza(Travoyad):
    def __init__(self, age, colorGreen, n, size):
        super().__init__(age, colorGreen, n)
        self.size = size

ml = Mlekopit(12)
tr = Travoyad(10, 'green', 6)
cow = Korova(5, 'yellow', 2, 3)
tr.eatgreen()
cow.eatgreen()
koza = Koza(5, 'yellow', 2, 3)
koza.eatgreen()

cow.eatmilk()
koza.eatmilk()

li = []
li.append(ml)
li.append(tr)
li.append(cow)
li.append(koza)

print("##############")
print(cow)



for el in li:
    print('------')
    # issubclass(Travoyad, el)
    print(type(el))
    if isinstance(el, Travoyad):
        print(type(el).mro())
        el.eatgreen()

# cow1 = Korova()
# cow1.eatgreen()

# tr1 = Travoyad()

class User:
    def __init__(self, login='', password='') -> None:
        self.login = login
        self.password = self.__genPassword()
        self._n = 8

    def __genPassword(self):
        return 123

class UserProfile(User):
    def __init__(self, login='', password='', email='', address='Ukraine') -> None:
        super().__init__(login, password)
        self.email = email
        self.address = address
        self._n += 1

u = User()

up = UserProfile(email='email', login='qwertyu')
print(up.address)
 
#----------------------------------------
