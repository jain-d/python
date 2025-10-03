import asyncio
from enum import Enum

class State(Enum):
    GoingUp = "up"
    GoingDown = "down"
    Idle = "idle"
    DoorOpen = "open"
    Reached = "reached"

class ElevatorFSM:
    def __init__(self):
        self.__floors: int = 12
        self.__current_floor: int = 0
        self.__elevator_state: State = State.Idle

    async def go_to(self, floor):
        try:
            floor = int(floor)
        except ValueError:
            print(f"\n\033[1;31mIncorrect Entry\033[0m, enter a number between 0 - 11, except {self.__current_floor}")
            return

        if self.__elevator_state != State.Idle:
            pass
        elif (floor < 0 or floor >= self.__floors) or floor == self.__current_floor:
            print("\n\033[1;31mInvalid Entry\033[0m, Please Try again")
        else:
            await self._door_functionality()
            await self._elevator_mechanics(floor)

    async def _elevator_mechanics(self, floor):
        travel_duration = abs(floor - self.__current_floor)
        self.__elevator_state = State.GoingUp if floor > self.__current_floor else State.GoingDown
        for _ in range(travel_duration):
            await self._changing_floors()
        print(f"\n\t\033[1;32mREACHED\033[0m!\n")
        self.__elevator_state = State.Reached
        await self._door_functionality()

    async def _changing_floors(self):
        if self.__elevator_state == State.GoingUp:
            await asyncio.sleep(2)
            self.__current_floor += 1
        else:
            await asyncio.sleep(1)
            self.__current_floor -= 1
        print(f"\nElevator at Floor \033[34m{self.__current_floor}\033[0m")

    async def _door_functionality(self):
        if self.__elevator_state == State.Reached or self.__elevator_state == State.Idle:
            self.__elevator_state = State.DoorOpen
            await asyncio.gather(self._door_animation(), asyncio.sleep(3))
            self.__elevator_state = State.Idle
            await self._door_animation()
        else:
            print("\n\033[31mINVALID OPERATION\033[0m")
            return

    async def _door_animation(self):
        if self.__elevator_state == State.DoorOpen:
            for index in range(5, -1, -1):
                print(f"\r<=={("=" * index):<5}  Door Opens!  {("=" * index):>5}==>", end="", flush=True)
                await asyncio.sleep(0.3)
        else:
            for index in range(5):
                arrow_extention = "=" * index
                right_side_arrow = "<==" + arrow_extention
                left_side_arrow = arrow_extention + "==>"
                print(f"\r{left_side_arrow:<8}  Door Closes  {right_side_arrow:>8}", end="", flush=True)
                await asyncio.sleep(0.3)

    @property
    def current_floor(self):
        return self.__current_floor


async def main():
    lift_man = ElevatorFSM()
    should_exit = False
    while not should_exit:
        print(f"\non level \033[1;31m{lift_man.current_floor}\033[0m")
        call_status = input("\n------ press \033[33m<Enter>\033[0m to call the lift, and \033[31mx\033[0m to exit ------ ")
        if call_status.strip().lower() == "x":
            break
        destination_floor = input("\rWhich floor sir? ")
        if destination_floor.strip().lower() == "x":
            break
        await lift_man.go_to(destination_floor)                         # intentionally passing string, lift_man will take care

if __name__ == "__main__":
    asyncio.run(main())
