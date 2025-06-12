# 1. Vehicle -> license_plate - Enum VehicleType{Car, Bus, Bike} - get_type(), fee_rate()
import itertools
from enum import Enum
import uuid
import time
from abc import ABC

class VehicleType(Enum):
  CAR = 1
  TRUCK = 2
  BIKE = 3

class Vehicle:
  def __init__(self, license_plate, vehicle_type):
    self.license_plate = license_plate
    self.vehicle_type = vehicle_type

class Car(Vehicle):
  def __init__(self, license_plate):
    super().__init__(license_plate, VehicleType.CAR)
  
class Truck(Vehicle):
  def __init__(self, license_plate):
    super().__init__(license_plate, VehicleType.TRUCK)

class Bike(Vehicle):
  def __init__(self, license_plate):
    super().__init__(license_plate, VehicleType.BIKE)
  
# 2. Parking Spot -> is_available(), park(), unpark()
class ParkingSpot:
  def __init__(self, spot_number, vehicle_type):
    self.spot_number = spot_number
    self.vehicle_type = vehicle_type
    self.vehicle = None

  def is_available(self):
    return self.vehicle is None
  
  def park(self, vehicle):
    if self.is_available() and self.vehicle_type == vehicle.vehicle_type:
      self.vehicle = vehicle
      return True
    return False
  
  def unpark(self):
    self.vehicle = None

# 3. Parking Level -> get_available_spot(), get_available_spots()
class ParkingLevel:
  def __init__(self, level_number, spots):
    self.level_number = level_number
    self.spots = spots
    for spot in self.spots:
      spot.level_number = level_number
  
  def get_available_spot(self, vehicle_type):
    for spot in self.spots:
      if spot.is_available() and spot.vehicle_type == vehicle_type:
        return spot
    return None
  
  def get_available_spots(self, vehicle_type):
    return [spot.spot_number for spot in self.spots
                if spot.is_available() and spot.vehicle_type == vehicle_type]

# 4. Ticket -> ticket_id, vehicle, spot, entry and exit time, duration_hours()
class Ticket:
  def __init__(self, ticket_id, spot, vehicle):
    self.ticket_id = ticket_id
    self.spot = spot
    self.vehicle = vehicle
    self.entry_timestamp = time.time()
    self.exit_timestamp  = None

  def set_exit(self):
      self.exit_timestamp = time.time()
  
  def duration_hours(self):
    if self.exit_timestamp is None:
      raise ValueError("Ticket is still active")
    hours = (self.exit_timestamp - self.entry_timestamp) / 3600.0
    return hours if hours >= 1.0 else 1.0

# 5. Payment -> FeeStrategy,
from abc import ABC, abstractmethod

class FeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, ticket):
        """Compute the fee for a given ticket."""
        pass

class FlatRateFeeStrategy(FeeStrategy):
  def __init__(self, rate_per_hour=10.0):
    self.rate_per_hour = rate_per_hour
  
  def calculate_fee(self, ticket):
    return ticket.duration_hours() * self.rate_per_hour

# Optional
class VehicleBasedFeeStrategy(FeeStrategy):
  def __init__(self):
    self.rates =  {
            VehicleType.CAR:   20.0,
            VehicleType.BIKE:  10.0,
            VehicleType.TRUCK: 30.0,
        }
  
  def calculate_fee(self, ticket):
    rate = self.rates.get(ticket.vehicle.vehicle_type, 0)
    return ticket.duration_hours() * rate

# 6. Parking Lot -> levels, add_level(), admit_vehicle(), release_vehicle()
class ParkingLot:
  def __init__(self):
        self.levels         = []
        self.active_tickets = {}
        self.fee_strategy   = FlatRateFeeStrategy()
  
  def set_fee_strategy(self, strategy):
        self.fee_strategy = strategy

  def add_level(self, level):
    self.levels.append(level)
  
  def admit_vehicle(self, vehicle):
    for level in self.levels:
      spot = level.get_available_spot(vehicle.vehicle_type)
      if spot and spot.park(vehicle):
        ticket_id = str(uuid.uuid4())
        ticket = Ticket(ticket_id, spot, vehicle)
        self.active_tickets[ticket_id] = ticket
        return ticket
    raise Exception(f"No available spot for {vehicle.vehicle_type.name}")
  
  def release_vehicle(self, ticket_id):
    ticket = self.active_tickets.pop(ticket_id, None)
    if not ticket:
      raise Exception("Invalid ticket")
    ticket.set_exit()
    fee = self.fee_strategy.calculate_fee(ticket)
    ticket.spot.unpark()
    return fee
  
  def display_availability(self):
        for level in self.levels:
            free = sum(1 for s in level.spots if s.is_available())
            total = len(level.spots)
            print(f"Level {level.level_number} — {free}/{total} spots free")

class SpotFactory:
    def __init__(self, prefix="S"):
        self._counter = itertools.count(1)
        self.prefix   = prefix

    def make_spot(self, vehicle_type):
        spot_id = f"{self.prefix}{next(self._counter)}"
        return ParkingSpot(spot_id, vehicle_type)

def main():
    lot1 = ParkingLot()
    factory = SpotFactory("L1-") 
    # build levels and spots for lot1
    spots1 = [factory.make_spot(VehicleType.CAR),
              factory.make_spot(VehicleType.CAR),
              factory.make_spot(VehicleType.BIKE),
              factory.make_spot(VehicleType.TRUCK)]
    level1 = ParkingLevel(1, spots1)
    lot1.add_level(level1)

    # build levels and spots for lot1
    factory = SpotFactory("L2-") 
    spots2 = [factory.make_spot(VehicleType.TRUCK),
              factory.make_spot(VehicleType.TRUCK)]
    level2 = ParkingLevel(2, spots2)
    lot1.add_level(level2)

    # switch fee strategy on lot1
    lot1.set_fee_strategy(FlatRateFeeStrategy())
    print("Lot1 availability:")
    lot1.display_availability()

    # park vehicles in lot1
    t1 = lot1.admit_vehicle(Car("CAR-AAA"))
    t2 = lot1.admit_vehicle(Bike("BIKE-BBB"))
    t3 = lot1.admit_vehicle(Truck("TRUCK-CCC"))
    print("After admit:")
    lot1.display_availability()

    # unpark from lot1
    fee1 = lot1.release_vehicle(t1.ticket_id)
    print(f"Unparked CAR-AAA from level {t1.spot.level_number}, fee = ${fee1:.2f}")
    lot1.display_availability()

if __name__ == "__main__":
    main()