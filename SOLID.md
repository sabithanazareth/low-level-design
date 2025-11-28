# SOLID Principles

- S.O.L.I.D. is a set of 5 principles that make software designs more maintainable, extensible, and robust.

## 1. S – Single Responsibility Principle (SRP)

➡ A class should have only one reason to change (do one thing well).

❌ Bad example (mixes multiple responsibilities):
```python
class Report:
    def __init__(self, content):
        self.content = content

    def format_report(self):   # formatting
        return f"Report: {self.content}"

    def save_to_file(self, filename):   # saving
        with open(filename, "w") as f:
            f.write(self.content)
``` 

✅ Good example (separate concerns):
```python
class Report:
    def __init__(self, content):
        self.content = content

class ReportFormatter:
    def format(self, report):
        return f"Report: {report.content}"

class ReportSaver:
    def save(self, report, filename):
        with open(filename, "w") as f:
            f.write(report.content)

```
- Now Report = data, Formatter = formatting, Saver = persistence.

## 2. O – Open/Closed Principle (OCP)

➡ Classes should be open for extension but closed for modification.

❌ Bad example:
```python
class Discount:
    def apply(self, customer_type, price):
        if customer_type == "regular":
            return price * 0.9
        elif customer_type == "vip":
            return price * 0.8
```
Adding new customer types requires modifying this class.

✅ Good example (extend with new classes, don’t modify old):
```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price):
        pass

class RegularDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.9

class VipDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.8

def get_price(strategy: DiscountStrategy, price):
    return strategy.apply(price)
```

- To add a new discount type, just create a new class.

## 3. L – Liskov Substitution Principle (LSP)

➡ Subtypes must be substitutable for their base types without breaking functionality.

❌ Bad example:
```python
class Bird:
    def fly(self):
        print("Flying")

class Ostrich(Bird):   # ostrich can't fly
    def fly(self):
        raise Exception("I can't fly!")
```

Violates LSP → Ostrich is not a proper substitute for Bird.

✅ Good example (separate hierarchy):
```python
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def run(self):
        print("Running fast")
```
# Now Ostrich doesn’t break expectations

## 4. I – Interface Segregation Principle (ISP)

➡ Don’t force classes to implement methods they don’t use.

❌ Bad example:
```python
class Worker:
    def work(self):
        pass
    def eat(self):
        pass

class Robot(Worker):
    def eat(self):
        raise Exception("Robots don’t eat")
```

Robot is forced to implement eat.

✅ Good example (smaller, role-specific interfaces):
```python
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Working")
    def eat(self):
        print("Eating")

class Robot(Workable):
    def work(self):
        print("Working")
```
## 5. D – Dependency Inversion Principle (DIP)

➡ High-level modules should not depend on low-level modules, both should depend on abstractions.

❌ Bad example:
```python
class MySQLDatabase:
    def save(self, data):
        print("Saving to MySQL")

class DataProcessor:
    def __init__(self):
        self.db = MySQLDatabase()   # tight coupling
    def process(self, data):
        self.db.save(data)
```

✅ Good example (use abstraction):

from abc import ABC, abstractmethod
```python
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print("Saving to MySQL")

class MongoDB(Database):
    def save(self, data):
        print("Saving to MongoDB")

class DataProcessor:
    def __init__(self, db: Database):   # depends on abstraction
        self.db = db
    def process(self, data):
        self.db.save(data)

# Usage
processor = DataProcessor(MySQLDatabase())
processor.process("my data")
```

- We can swap MySQL with MongoDB without changing DataProcessor.

✅ Recap (SOLID in one line each)

S – Single Responsibility: One class = one job.
O – Open/Closed: Add new features by extension, not modification.
L – Liskov Substitution: Subclasses should work wherever parent is expected.
I – Interface Segregation: Many small interfaces > one big interface.
D – Dependency Inversion: Depend on abstractions, not concrete classes.