# Elevator system low-level-design

Discuss basic workflow:

1. Building has floors and elevator
2. User presses the direction and enters the elevator
3. The destination(floor) number is pressed
4. Elevator is stopped at the destination and user exits

Requirements:

1. Multiple Elevator: The system manages multiple elevators.
2. Request Handling: The system can handle requests to move to specific floors in a given direction (UP/DOWN).
3. Direction Management: The elevator maintains and updates its current direction (UP, DOWN, IDLE).
4. State Management: The elevator tracks its current floor, direction, and pending requests.
5. Efficient Movement: The elevator processes requests in an efficient order (e.g., all UP requests, then all DOWN requests).

Identify Entities:

1. Elevator: Represents the elevator, manages its state, direction, and request queue.
2. ElevatorController: Handles incoming requests and delegates them to the elevator.
3. Request: Represents a request to move to a specific floor in a given direction.
4. Direction (enum): UP, DOWN, IDLE.

Class Design

1. Elevator
   Fields: currentFloor, direction, List requests, isMoving, etc.
   Methods: addRequest(Request), move(), openDoor(), closeDoor(), processNextRequest(), getCurrentFloor(), getDirection(), etc.
2. ElevatorController
   Fields: Elevator elevator
   Methods: requestElevator(int floor, Direction direction), step(), etc.
3. Request
   Fields: int floor, Direction direction
4. Direction (enum)
   Values: UP, DOWN, IDLE
