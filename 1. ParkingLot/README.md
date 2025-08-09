# Parking Lot low-level-design

Discuss basic workflow:

1. 1 parking lot with levels and each level has mulitple spots
2. Vehicle enters parking lot through the entry gate
3. Gets a ticket
4. Parks vehicle at a free spot
5. Unpark and go to the exit gate
6. Make the payment and exit

Requirements:

1. Multiple Floors: The parking lot can have multiple levels, each with its own set of spots.
2. Parking Spots: Each level has parking spots typed for Cars, Trucks, or Bikes.
3. Vehicle Types: Support for different vehicle types via a `VehicleType` enum and concrete `Vehicle` subclasses.
4. Ticketing: Generate a unique ticket (with entry timestamp and spot info) when a vehicle parks.
5. Unparking & Fee Calculation: On unpark, record exit time, compute duration (minimum 1 hour), and calculate fee via a configurable strategy.
6. Spot Allocation: Always allocate the nearest (first-found) available spot matching the vehicle’s type.

Identify Entities and Class Design:

1. Vehicle -> license_plate - Enum VehicleType{Car, Bus, Bike} - get_type(), fee_rate()
2. Parking Lot -> levels, add_level(), admit_vehicle(), release_vehicle()
3. Parking Level -> spots, get_available_spot(), get_available_spots()
4. Parking Spot -> is_available(), park(), unpark()
5. Ticket -> ticket_id, vehicle, spot, entry and exit time, duration_hours()
6. SpotFactory -> prefix, make_spot()
7. Payment -> FeeStrategy

Patterns Used:

1. Factory Pattern - make_spot() encapsulates the creation of ParkingSpot objects
2. Strategy Pattern - FeeStrategy
