# Instead of the client code directly creating objects, it delegates the responsibility to a Factory Method. Create objects without specifying excat class. Create objects based on conditions
# Ex - French, Spanish and English Localizer for words

# Product
from abc import ABC, abstractmethod

# Step 1: Defining the Product
class Localizer(ABC):
    """Abstract Product: Represents translations for specific languages."""
    @abstractmethod
    def localize(self, msg):
        """Translate the given message."""
        pass

#Concrete Products:
# Step 2: Creating Concrete Products
class FrenchLocalizer(Localizer):
    """Concrete Product: Represents translations for French."""
    def __init__(self):
        self.translations = {
          "car": "voiture",
          "bike": "bicyclette",
          "cycle": "cyclette"
        }

    def localize(self, msg):
        """Translate the message to French."""
        return self.translations.get(msg, msg)

class SpanishLocalizer(Localizer):
    """Concrete Product: Represents translations for Spanish."""
    def __init__(self):
        self.translations = {
          "car": "coche",
          "bike": "bicicleta",
          "cycle": "ciclo"
        }

    def localize(self, msg):
        """Translate the message to Spanish."""
        return self.translations.get(msg, msg)

class EnglishLocalizer(Localizer):
    """Concrete Product: Represents translations for English."""
    def localize(self, msg):
        """Return the message as is (no translation)."""
        return msg

#Creator
# Step 3: Defining the Creator
def create_localizer(language="English"):
    """
    Factory Method: Create a localizer for the specified language.

    Args:
        language (str): The language for which to create a localizer.

    Returns:
        Localizer: An instance of the localizer for the specified language.
    """
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }
    return localizers[language]()

# Utilizing Factory
# Step 4: Utilizing the Factory
if __name__ == "__main__":
    # Create localizers for different languages
    french_localizer = create_localizer("French")
    english_localizer = create_localizer("English")
    spanish_localizer = create_localizer("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        # Print localized messages for each language
        print(french_localizer.localize(msg))
        print(english_localizer.localize(msg))
        print(spanish_localizer.localize(msg))