class Car:
    price = 1000000

    def horse_powers(self, power):
        return power


class Nissan(Car):
    price = 2000000

    def horse_powers(self, power):
        return f'Цена {self.price} и мощность в л.с. {power}'

class Kia(Car):
    price = 3000000

    def horse_powers(self, power):
        return f'Мощность в л.с. {power} и цена {self.price}'

nis = Nissan()
kia = Kia()
print(nis.horse_powers(200))
print(kia.horse_powers(100))
