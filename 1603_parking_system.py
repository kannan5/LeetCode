class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, car_type) -> bool:
        if car_type == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False
        if car_type == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                return False
        if car_type == 3:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False

class ParkingSystemArr:
    def __init__(self, big: int, medium: int, small: int):
        self.arr = [big, medium, small]

    def AddCar(self, car_type):
        self.arr[car_type - 1] -= 1
        return self.arr[car_type - 1] >= 0



class ParkingSystemDict:
    def __init__(self, big: int, medium: int, small: int):
        self.spaces = {1:big, 2: medium, 3: small}


    def addCar(self, carType: int) -> bool:
        if self.spaces[carType] == 0:
            return False
        else:
            self.spaces[carType] -= 1
            return True