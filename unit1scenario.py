# ============================================================
# UNIT 1 - SCENARIO 4 & SCENARIO 6
# Mobile Store Management System + Vehicle Showroom Management
# ============================================================


# ============================================================
# 4. MOBILE STORE MANAGEMENT SYSTEM
# ============================================================

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def category(self):
        if self.price >= 70000:
            return "Premium"
        elif self.price >= 30000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price: ₹", self.price)
        print("Category:", self.category())
        print()


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_mobiles(self):
        print("----- MOBILE STORE -----")
        for mobile in self.mobiles:
            mobile.display()


# ============================================================
# 6. VEHICLE SHOWROOM MANAGEMENT SYSTEM
# ============================================================

class Vehicle:
    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price

    def category(self):
        if self.price >= 1000000:
            return "Luxury"
        else:
            return "Economy"

    def display(self):
        print("Vehicle Number:", self.vehicle_number)
        print("Brand:", self.brand)
        print("Price: ₹", self.price)
        print("Category:", self.category())
        print()


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        print("----- VEHICLE SHOWROOM -----")
        for vehicle in self.vehicles:
            vehicle.display()


# ============================================================
# MAIN PROGRAM
# ============================================================

# Creating Mobile Store
store = Store()

mobile1 = Mobile("Apple", "iPhone 15", 80000)
mobile2 = Mobile("Samsung", "Galaxy A55", 45000)
mobile3 = Mobile("Redmi", "Note 13", 20000)

store.add_mobile(mobile1)
store.add_mobile(mobile2)
store.add_mobile(mobile3)

# Display all mobiles
store.display_mobiles()


# Creating Vehicle Showroom
showroom = Showroom()

vehicle1 = Vehicle("MH12AB1234", "BMW", 1500000)
vehicle2 = Vehicle("MH14CD5678", "Maruti", 800000)
vehicle3 = Vehicle("MH15EF9012", "Hyundai", 700000)

showroom.add_vehicle(vehicle1)
showroom.add_vehicle(vehicle2)
showroom.add_vehicle(vehicle3)

# Display all vehicles
showroom.display_vehicles()


# ============================================================
# OUTPUT
# ============================================================

# ----- MOBILE STORE -----
# Brand: Apple
# Model: iPhone 15
# Price: ₹ 80000
# Category: Premium
#
# Brand: Samsung
# Model: Galaxy A55
# Price: ₹ 45000
# Category: Mid-range
#
# Brand: Redmi
# Model: Note 13
# Price: ₹ 20000
# Category: Budget
#
# ----- VEHICLE SHOWROOM -----
# Vehicle Number: MH12AB1234
# Brand: BMW
# Price: ₹ 1500000
# Category: Luxury
#
# Vehicle Number: MH14CD5678
# Brand: Maruti
# Price: ₹ 800000
# Category: Economy
#
# Vehicle Number: MH15EF9012
# Brand: Hyundai
# Price: ₹ 700000
# Category: Economy