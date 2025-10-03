from enum import Enum

class DoorStateMachine:
    def __init__(self):
        self.Possible_states = Enum("Possible_states", ["Locked", "Open", "Unlocked"])
        self.door_state = self.Possible_states.Locked

    def trigger(self, event: str):
        match event:
            case "insert_key":
                if self.door_state == self.Possible_states.Locked:
                    self.door_state = self.Possible_states.Unlocked
                    print("DOOR UnLocked")
                else:
                    print("\033[1;31mINVALID ACTION\033[0m")

            case "open_door":
                if self.door_state == self.Possible_states.Unlocked:
                    self.door_state = self.Possible_states.Open
                    print("DOOR Opened")
                else:
                    print("\033[1;31mINVALID ACTION\033[0m")

            case "close_door":
                if self.door_state == self.Possible_states.Open:
                    self.door_state = self.Possible_states.Unlocked
                    print("Closed DOOR, BUT UnLocked")
                else:
                    print("\033[1;31mINVALID ACTION\033[0m")

            case "remove_key":
                if self.door_state == self.Possible_states.Unlocked:
                    self.door_state = self.Possible_states.Locked
                    print("DOOR Locked")
                else:
                    print("\033[1;31mINVALID ACTION\033[0m")

            case _:
                print("\033[1;31mINVALID ACTION\033[0m")

door = DoorStateMachine()

door.trigger("insert_key")
door.trigger("close_door")
