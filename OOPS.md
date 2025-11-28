## 1. Encapsulation

### Idea: Bundle data (variables) and behavior (methods) into a single unit (class). Control access to internal details using public/private methods.

```python
 class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private variable (encapsulated)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):  # controlled access
        return self.__balance

acc = BankAccount("Alice", 1000)
acc.deposit(500)
print(acc.get_balance())   # 1500
# print(acc.__balance) → ERROR (protected by encapsulation)
```


## 2. Inheritance

### Idea: A class can inherit attributes and behaviors from another class (base/parent → child/derived). Promotes code reuse.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        print("This vehicle is moving")

class Car(Vehicle):   # inherits from Vehicle
    def honk(self):
        print("Beep beep!")

car = Car("Toyota")
car.drive()   # inherited from Vehicle
car.honk()    # defined in Car
```

## 3. Polymorphism

### Idea: Same method name but different behavior depending on the object.

#### Compile-time (overloading): Not common in Python (simulated using default args).

#### Runtime (overriding): Child class redefines a parent class method.

```python
class Animal:
    def speak(self):
        print("This animal makes a sound")

class Dog(Animal):
    def speak(self):    # override
        print("Woof!")

class Cat(Animal):
    def speak(self):    # override
        print("Meow!")

animals = [Dog(), Cat()]
for a in animals:
    a.speak()   # Different behavior (Woof! Meow!)
```

## 4. Abstraction

### Idea: Hiding implementation details, showing only what’s necessary. Achieved via abstract classes or interfaces.

```python
from abc import ABC, abstractmethod

class Shape(ABC):       # abstract class
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

shapes = [Circle(5), Square(4)]
for s in shapes:
    print(s.area())   # 78.5, 16
```