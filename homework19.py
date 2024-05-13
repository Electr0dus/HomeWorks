class Car:
    price = 1000000

    def horse_powers(self):
        return 100


class Nissan(Car):
    price = 2000000

    def horse_powers(self):
        return 200


class Kia(Car):
    price = 3000000

    def horse_powers(self):
        return 300


nis = Nissan()
kia = Kia()
print(nis.horse_powers())
print(kia.horse_powers())
