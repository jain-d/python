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
