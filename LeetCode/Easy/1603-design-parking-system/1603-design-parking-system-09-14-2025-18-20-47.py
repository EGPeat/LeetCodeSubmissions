class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.spots = [big, medium, small]

    def addCar(self, car_type: int) -> bool:
        if self.spots[car_type - 1] > 0:
            self.spots[car_type - 1] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)