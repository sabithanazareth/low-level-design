
# To ensure that a class has only one instance throughout the application’s lifecycle.
class RentalSystem:
  _instance = None
  def __init__(self):
    if RentalSystem._instance is not None:
      raise Exception("This class is a singleton!")
    else:
      RentalSystem._instance = self
      self.cars = {}
      self.reservations = {}
  
  @staticmethod
  def get_instance():
    if RentalSystem._instance is None:
        RentalSystem()
    return RentalSystem._instance

class CarRentalSystem:
  @staticmethod
  def run():
    rental_system = RentalSystem.get_instance()