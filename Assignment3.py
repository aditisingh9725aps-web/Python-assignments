from abc import ABC, abstractmethod

# ==========================================
# STRATEGY DESIGN PATTERN - PAYMENT SYSTEM
# ==========================================

# Strategy Interface
class PaymentMethod(ABC):

    @abstractmethod
    def make_payment(self, amount):
        pass


# Strategy 1
class CardPayment(PaymentMethod):

    def make_payment(self, amount):
        print(f"Payment of Rs {amount} completed using Credit Card.")


# Strategy 2
class DebitPayment(PaymentMethod):

    def make_payment(self, amount):
        print(f"Payment of Rs {amount} completed using Debit Card.")


# Strategy 3
class UPITransfer(PaymentMethod):

    def make_payment(self, amount):
        print(f"Payment of Rs {amount} completed using UPI.")


# Strategy 4
class BankTransfer(PaymentMethod):

    def make_payment(self, amount):
        print(f"Payment of Rs {amount} completed using Net Banking.")


# Context Class
class PaymentGateway:

    def __init__(self, method=None):
        self.method = method

    def choose_method(self, method):
        self.method = method

    def pay_bill(self, amount):
        if self.method is None:
            print("No payment method selected.")
        else:
            self.method.make_payment(amount)


# Driver Code
gateway = PaymentGateway()

while True:
    print("\n===== Online Payment Menu =====")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Net Banking")
    print("5. Exit")

    try:
        option = int(input("Choose an option: "))

        if option == 5:
            print("Exiting Payment System...")
            break

        if option not in [1, 2, 3, 4]:
            print("Invalid option! Please try again.")
            continue

        amount = float(input("Enter amount: "))

        if option == 1:
            gateway.choose_method(CardPayment())
        elif option == 2:
            gateway.choose_method(DebitPayment())
        elif option == 3:
            gateway.choose_method(UPITransfer())
        elif option == 4:
            gateway.choose_method(BankTransfer())

        gateway.pay_bill(amount)

    except ValueError:
        print("Please enter valid numeric values.")


# ---------------- SAMPLE OUTPUT ----------------
#
# ===== Online Payment Menu =====
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Choose an option: 1
# Enter amount: 500
# Payment of Rs 500.0 completed using Credit Card.
#
# ===== Online Payment Menu =====
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Choose an option: 3
# Enter amount: 1200
# Payment of Rs 1200.0 completed using UPI.
#
# ===== Online Payment Menu =====
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Choose an option: 4
# Enter amount: 850
# Payment of Rs 850.0 completed using Net Banking.
#
# ===== Online Payment Menu =====
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# 5. Exit
# Choose an option: 5
# Exiting Payment System...