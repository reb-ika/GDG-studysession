class Vehicle:
    def init(self, make, model, plate_number):
        self.make = make
        self.model = model
        self.__plate_number = plate_number  # Private attribute

    def get_plate_number(self):  # Getter method to access private attribute
        return self.__plate_number

    def describe(self):
        return f"This is a {self.make} {self.model} with plate number {self.get_plate_number()}."

class Car(Vehicle):
    def init(self, make, model, plate_number, num_doors):
        super().init(make, model, plate_number)  # Inherit parent attributes
        self.num_doors = num_doors

    def describe(self):  # Override describe() of the super class
        return f"This is a {self.make} {self.model} with {self.num_doors} doors."

class Bike(Vehicle):
    def describe(self):
        return f"This is a {self.make} {self.model} bike."


vehicle = Vehicle("Toyota", "Corolla", "ABC-123")
car = Car("Toyota", "Corolla", "XYZ-456", 4)
bike = Bike("Yamaha", "MT-07", "MNO-789")


print(vehicle.describe())
print(car.describe())
print(bike.describe())
