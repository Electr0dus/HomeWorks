class Vehicle:
    vehicle_type="none"

class Car:
    price = 1000000

    def horse_powers(self):
        return 200

class Nissan(Car, Vehicle):
    price = 2000000
    vehicle_type = "UNnone"
    def horse_powers(self):
        return 300

nis = Nissan()
print(nis.vehicle_type)
print(nis.price)