# For once and for all

class House:
    def __init__(self, words, location) -> None:
        self.words = words 
        self.location = location
    
    def say_words(self):
        print(self.words)

    def where(self):
        print(self.location)

starks = House("winter in comming", "Winterfell")
lannisters = House("a lannister always pays his debts", "Casterly Rock")
baratheon = House("ours is the fury", "Dragonstone")

print("\n")
print(starks)
print(lannisters)
