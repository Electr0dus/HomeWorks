class Buiding:
    def __init__(self):
        self.numberOfFloors = 0
        self.buildingType = '0'

    def __eq__(self, other):
        one = self.numberOfFloors == other.numberOfFloors
        second = self.buildingType == other.buildingType
        return one and second

