import random # imports random mod to generate random numbers

class Armor:
    # created class to initialize armor with name and block value
    def __init__(self, name, max_block):
        self.name = name # name of armor
        self.max_block = max_block # max block value armor can provide

    def block(self):
        '''Returns a random a random value between 0 and max_block'''
        # creates a sim of blocking an attack so it returns a random value up to max block
        return random.randint(0, self.max_block)
    
if __name__ == "__main__":
    # this is an example thing to call directly
    shield = Armor("Shield", 30)
    print(shield.block())