# Parking Lot low-level-design

Discuss basic workflow:

1. 1 parking lot with levels and each level has mulitple spots
2. Vehicle enters parking lot through the entry gate
3. Gets a ticket
4. Parks vehicle at a free spot
5. Unpark and go to the exit gate
6. Make the payment and exit

Clarify requirements:

1. One parking lot?
2. Are there levels in this parking lot or its just ground level?
3. Do we need different spot size for different vehicles?
4. Can I assume we have Car, Bus, Motorcycle for now?

Identify Entities:

1. Vehicle -> license_plate - Enum VehicleType{Car, Bus, Bike} - get_type(), fee_rate()
2. Parking Lot -> levels, add_level(), admit_vehicle(), release_vehicle()
3. Parking Level -> get_available_spot(), get_available_spots()
4. Parking Spot -> is_available(), park(), unpark()
5. Ticket -> ticket_id, vehicle, spot, entry and exit time, duration_hours()
6. Payment -> FeeStrategy,
