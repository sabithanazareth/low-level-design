# To allow dynamic selection by a client class

from abc import ABC, abstractmethod

# Step 1: Define Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Step 2: Implement Different Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Cryptocurrency")

# Step 3: Context uses a Strategy
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def process_payment(self, amount):
        self.strategy.pay(amount)

# Step 4: Client chooses strategy at runtime
processor = PaymentProcessor(PayPalPayment())
processor.process_payment(100)   # Paid 100 using PayPal

processor = PaymentProcessor(CreditCardPayment())
processor.process_payment(200)   # Paid 200 using Credit Card

processor = PaymentProcessor(CryptoPayment())
processor.process_payment(300)   # Paid 300 using Cryptocurrency
