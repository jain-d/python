class Vehical:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

class Car(Vehical):
    wheels = 4

    def __init__(self, name, engine_type):
        self.engine_type = engine_type
        super().__init__(name)

    def move(self):
        self.print_name()
        print(f"this {self.engine_type} engine car runs on {self.wheels} wheels")

slavia = Car("Slavia", "turbo")
slavia.move()


