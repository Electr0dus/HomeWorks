class House:
    def __init__(self):
        self.numberOfFloors = 10


myHouse = House()
for i in range(1, myHouse.numberOfFloors + 1):
    print(f'Текущей этаж равен {i}')