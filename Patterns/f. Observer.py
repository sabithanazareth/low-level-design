# When something changes, let everyone who’s interested know automatically. Youtube subscription, stock price

# Step 1: Define Subject (publisher)
class Subject:
    def __init__(self):
        self._observers = []  # list of subscribers
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# Step 2: Define Observer Interface
class Observer:
    def update(self, message):
        pass

# Step 3: Create Concrete Observers
class EmailSubscriber(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"Email to {self.name}: {message}")

class SMSSubscriber(Observer):
    def __init__(self, phone):
        self.phone = phone
    
    def update(self, message):
        print(f"SMS to {self.phone}: {message}")

# Step 4: Client 
# Create subject (e.g., YouTube Channel)
channel = Subject()

# Add subscribers
email_user = EmailSubscriber("Alice")
sms_user = SMSSubscriber("+1234567890")

channel.attach(email_user)
channel.attach(sms_user)

# Notify all observers
channel.notify("New video uploaded!")  

# Output:
# Email to Alice: New video uploaded!
# SMS to +1234567890: New video uploaded!
