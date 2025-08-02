Basic workflow:

1. User goes to CarRental company and asks for Car to rent.
2. User is given the car for the requested date and pays for it
3. Returns the car on the last day
4. If not penalty
5. Charge for any damages

Requirements:

1. Allow customers to browse and reserve available cars for specific dates.
2. Each car should have details such as make, model, year, license plate number, and rental price per day.
3. Customers should be able to search for cars based on various criteria, such as car type, price range, and availability.
4. Handle reservations, including creating, modifying, and canceling reservations
5. Keep track of the availability of cars and update their status accordingly.
6. Handle customer information, including name, contact details, and driver's license information.
7. Handle payment processing for reservations.

Core Entities:

1. RentalSystem - adding and removing cars, searching for available cars based on criteria, making reservations, canceling reservations, and processing payments.
2. CarType(ABC) - Standard, Electric, Luxury
3. Car - make, model, year, license plate number, rental price per day, and availability status.
4. Customer - name, contact information, and driver's license number.
5. Reservation - reservation ID, customer, car, start date, end date, and total price.
6. Payment - FeeStrategy
