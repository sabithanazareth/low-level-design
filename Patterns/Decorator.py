# It enables you to “decorate” or enhance objects by adding new functionalities without modifying their structure.
# When to Use the Decorator Pattern
# Add Responsibilities Dynamically: When you want to add behavior or features to objects dynamically at runtime without modifying their code.
# Avoid a Complex Inheritance Hierarchy (Class Explosion): To avoid creating a deep and complex class hierarchy through subclassing, which can be challenging to maintain.
# when there is a lot of combination BasePizza + Cheese + Mushrrom, BasePizza + Jalapeno, BasePizza + Mushroom

# Ex:
# - Game design where different characters possess a unique set of abilities.
# - Game character abilities, such as the DoubleDamageDecorator, FireballDecorator, and InvisibilityDecorator.

from abc import ABC, abstractmethod

# ——— Component Interface ———
class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        """Returns a description of the pizza."""
        pass

    @abstractmethod
    def get_cost(self) -> float:
        """Returns the total cost of the pizza."""
        pass


# ——— Concrete Component ———
class PlainPizza(Pizza):
    def get_description(self) -> str:
        return "Plain pizza"

    def get_cost(self) -> float:
        return 5.00  # base price


# ——— Decorator Base ———
class PizzaDecorator(Pizza):
    def __init__(self, wrapped: Pizza):
        self._wrapped = wrapped

    def get_description(self) -> str:
        return self._wrapped.get_description()

    def get_cost(self) -> float:
        return self._wrapped.get_cost()


# ——— Concrete Decorators ———
class CheeseDecorator(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self._wrapped.get_description()}, + cheese"

    def get_cost(self) -> float:
        return self._wrapped.get_cost() + 1.25


class PepperoniDecorator(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self._wrapped.get_description()}, + pepperoni"

    def get_cost(self) -> float:
        return self._wrapped.get_cost() + 1.50


class OlivesDecorator(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self._wrapped.get_description()}, + olives"

    def get_cost(self) -> float:
        return self._wrapped.get_cost() + 0.75


# ——— Client Code ———
if __name__ == "__main__":
    # start with a plain pizza
    pizza: Pizza = PlainPizza()
    print(pizza.get_description(), f"${pizza.get_cost():.2f}")

    # add cheese
    pizza = CheeseDecorator(pizza)
    print(pizza.get_description(), f"${pizza.get_cost():.2f}")

    # add pepperoni
    pizza = PepperoniDecorator(pizza)
    print(pizza.get_description(), f"${pizza.get_cost():.2f}")

    # add olives
    pizza = OlivesDecorator(pizza)
    print(pizza.get_description(), f"${pizza.get_cost():.2f}")
