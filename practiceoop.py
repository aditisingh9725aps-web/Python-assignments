#vechile managment system using oops 
# Parent Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle is starting")


# Child Class (Inheritance)
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.__model = model      # Encapsulation

    # Polymorphism (Method Overriding)
    def start(self):
        print(self.brand, self.__model, "is starting")

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.__model)


# Object Creation
car = Car("Toyota", "Fortuner")

car.display()
car.start()
'''
OUTPUT:

Brand: Toyota
Model: Fortuner
Toyota Fortuner is starting

'''


