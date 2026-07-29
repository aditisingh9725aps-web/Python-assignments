from abc import ABC, abstractmethod

# ==========================================
# FACTORY DESIGN PATTERN
# ==========================================

class Creature(ABC):
    @abstractmethod
    def sound(self):
        pass


class Puppy(Creature):
    def sound(self):
        return "Woof!"


class Kitten(Creature):
    def sound(self):
        return "Meow!"


class CreatureFactory:
    def get_creature(self, creature_type):
        if creature_type.lower() == "dog":
            return Puppy()
        elif creature_type.lower() == "cat":
            return Kitten()
        else:
            raise ValueError("Invalid creature type")


print("===== Factory Pattern =====")
factory = CreatureFactory()

dog = factory.get_creature("dog")
cat = factory.get_creature("cat")

print(dog.sound())
print(cat.sound())

# Output:
# ===== Factory Pattern =====
# Woof!
# Meow!


# ==========================================
# OBSERVER DESIGN PATTERN
# ==========================================

class NotificationCenter:
    def __init__(self):
        self.listeners = []

    def subscribe(self, listener):
        self.listeners.append(listener)

    def unsubscribe(self, listener):
        self.listeners.remove(listener)

    def broadcast(self, message):
        for listener in self.listeners:
            listener.receive(message)


class Listener:
    def receive(self, message):
        print("Notification:", message)


print("\n===== Observer Pattern =====")
center = NotificationCenter()

user1 = Listener()
user2 = Listener()

center.subscribe(user1)
center.subscribe(user2)

center.broadcast("Welcome to the Observer Pattern!")

# Output:
# ===== Observer Pattern =====
# Notification: Welcome to the Observer Pattern!
# Notification: Welcome to the Observer Pattern!


# ==========================================
# SINGLETON DESIGN PATTERN
# ==========================================

class DatabaseConnection:
    _obj = None

    def __new__(cls):
        if cls._obj is None:
            cls._obj = super().__new__(cls)
        return cls._obj


print("\n===== Singleton Pattern =====")
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)

# Output:
# ===== Singleton Pattern =====
# True


# ==========================================
# STRATEGY DESIGN PATTERN
# ==========================================

class Operation:
    def perform(self):
        raise NotImplementedError("Method must be implemented")


class AddOperation(Operation):
    def perform(self):
        return "Addition Strategy Selected"


class MultiplyOperation(Operation):
    def perform(self):
        return "Multiplication Strategy Selected"


class Calculator:
    def __init__(self, operation):
        self.operation = operation

    def execute(self):
        return self.operation.perform()


print("\n===== Strategy Pattern =====")
calc = Calculator(AddOperation())
print(calc.execute())

calc = Calculator(MultiplyOperation())
print(calc.execute())

# Output:
# ===== Strategy Pattern =====
# Addition Strategy Selected
# Multiplication Strategy Selected