import random # random numbers again

class Ability:
    # created a class to set up abilities with name and max dmg
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        # creates sim of using ability by returning random dmg value
        '''Return a random value between 0 and max_damage'''
        return random.randint(0, self.max_damage)

if __name__ == "__main__":
    # example again
    greaseball = Ability("greaseball", 50)
    print(greaseball.attack())