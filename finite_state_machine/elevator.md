# 🚧 Project Specification: Elevator Finite State Machine (FSM)

## 🎯 Objective

Build a Python-based Finite State Machine (FSM) that simulates the behavior of a simple elevator operating in a building with **12 floors (0–11)**. The elevator responds to user requests to move to a specific floor, handles time-based transitions, enforces constraints, and simulates realistic behavior.

---

## 🏢 System Overview

The elevator has:

* **One cabin**
* **No queuing system** (only one request can be handled at a time)
* **One user interface method**: `go_to(floor_number: int)`

---

## 🔢 Building Constraints

* The building has **12 floors**, numbered **0 to 11**
* Any request to move outside this range must be rejected
* If a user requests the **current floor**, the request must be ignored with a warning

---

## ⚙️ Elevator States (Enum)

1. `IDLE` — Elevator is waiting for a request
2. `MOVING_UP` — Elevator is moving up
3. `MOVING_DOWN` — Elevator is moving down
4. `DOOR_OPEN` — Elevator has reached target and opened doors

---

## 🧠 Behavior Logic

### ✔️ Accepting a Request:

* Only allowed in the `IDLE` state
* If target floor is invalid (not 0–11): print error
* If target floor == current floor: print message and do nothing
* Otherwise, transition to `MOVING_UP` or `MOVING_DOWN` based on direction

### ⬆️ Moving:

* Elevator moves **one floor at a time** toward the target
* **Time per floor**:

  * **2 seconds** if going up
  * **1 second** if going down
* Print each floor as the elevator moves

### 🚪 Opening the Door:

* When elevator reaches the target floor:

  * Print arrival message
  * Transition to `DOOR_OPEN`
  * Wait **3 seconds**
  * Close door and transition to `IDLE`

---

## 🛑 Invalid Scenarios

* Reject `go_to()` if:

  * Elevator is not in `IDLE` state
  * Floor number is out of bounds
  * Floor number is the same as current floor

---

## 🧪 Optional Extension Ideas (not required, but fun):

* Queue multiple floor requests
* Support for up/down buttons on each floor
* Emergency stop or maintenance state
* Asynchronous version with `asyncio`

---

## 📦 Deliverables

* `ElevatorFSM` class
* Can be run via a script or REPL (no GUI needed)
* Logs all state transitions, delays, and actions clearly in console

====================== SOLUTION ======================

To start with, we have an `ElevatorFSM` class that contains all the functionality of the elevator.

Next we have a class called `State` that inherits `enum.Enum`. This class contains 5 states, going up, going down, reached, door open, and idle. This is 1 mores states then we originally discussed.

Inside the elevator class, the constructor instantiate 3 fields, first for total number of floors, second for the current floor is lift is on, and the current elevator state.
Then I have a method called `go_to(floor: str)` method, which is the main method that fires all the different methods. This method takes in the value of floor, checks weather the floor is < total floors in the building and not equal to the current floor. If everything is correct, it proceeds to calls 2 methods(door_functionality and elevator_mechanics) one after the other.

door_functionality function is an interesting, because not only does it makes sure that door is open for 3 seconds, but it also calls another function called door animation, which asynchronously(as the door is open for the 3 seconds, utilizing the cooperative multitasking of python's asyncio.gather()) does a cool cli animation of the elevator door opening(a large arrows pointing in either direction contracts from the middle to either ends, just like an elevator door) and closing(small arrows pointing to the center enlarges in size coming both coming to the center to simulate a door close).

The elevator_mechanics function does the calculation of how many floor do we have to climb or decend, calls the changing_floors function repeatedly based on the number of floors, after we have reached, calls the door_functionality methods

changing_floors function takes care of the varying delay we need for ascending and decending floors and update the value of current_floor variable.

Lastly, a getter for current_floor.


Now the main function is where we create an object for ElevatorFSM, create an exit variable, and then I have an infinite loop that calls all the methods on the object of ElevatorFSM.


This is the overview for you, refrain any judgements for now. The next chat will contain the actual code.

======================= Next Steps ========================

Absolutely — here’s your original message, now reformatted as a **Next Steps** section for your `README.md`. This captures your thought process cleanly and can guide your future implementation work.

---

## Next Steps: Evolving the Elevator FSM into a GUI Simulation

While the current CLI-based FSM simulates a single user interacting with the elevator, there are limitations in visualizing **multiple concurrent interactions** and tracking **dynamic queue behavior**. The next phase of the project will involve expanding the system into a **multi-user, real-time simulation** using a GUI framework (mostly likely Tkinter).

### Goals for Next Phase:

1. **Implement Request Queuing**
   Introduce internal and external call queues that the elevator can serve based on direction, proximity, and time of request.

2. **Handle Concurrent User Perspectives**
   Support multiple "people" on different floors:

   * A user on floor 4 sees the elevator passing by
   * Another on floor 3 pressed the button earlier
   * Both requests are tracked and prioritized

3. **Introduce Decision-Making Logic**
   Build a smart decision engine to determine:

   * Which request should be served next
   * Whether to continue in the current direction or reverse
   * How to efficiently serve multiple queued calls

4. **Visualize System Behavior**
   CLI is limited in displaying live updates and concurrent events. A GUI will allow:

   * A view of the elevator moving between floors
   * Floor buttons lighting up when pressed
   * Doors opening and closing in real time
   * Live updates of the request queue
