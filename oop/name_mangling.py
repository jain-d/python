# Testing how can we modify private variable(name mangled) from outside of the class
class TestPrivate:
    __slots__ = ["__name", "__id"]
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __dir__(self):
        return ["1. SORRY", "2. can't", "3. view", "4. internal", "5. REP"]


mikey = TestPrivate("Michael", 45)

print(mikey.name)

#mikey._TestPrivate__name += " Chandler"                  # Even LSP was not able to catch the error here

#print(mikey.__dict__)

#mikey.__dict__["_TestPrivate__name"] += " Chandler"

print(dir(mikey))
