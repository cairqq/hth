import random
from ability import Ability
from armor import Armor
# this creates a class called hero that includes abilities and armor
class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name # hero name
        self.starting_health = starting_health # initial health
        self.current_health = starting_health  # current health is the same as starting
        self.abilities = [] # a list that holds ability objects
        self.armors = [] # a list that holds armor objects

    def battle(self, opponent):
        # simulates a battle between two heroes
    # '''Fight another hero and randomly declare a winner'''
        self.opponent = opponent # stores oppenent
        print(f"{self.name} battles {opponent.name}!") # announces battle
        # Randomly choose winner
        winner = random.choice([self, opponent]) 
        print(f"{winner.name} wins the battle!") # prints winner

    def add_ability(self, ability):
        '''Adds an ability to the existing abilities list'''
        self.abilities.append(ability) # adds the ability into list
        print(f"{ability.name} has been added to {self.name}'s list.") #prints ability into heros list

    def sum_of_attacks(self):
        '''Loops through abilities list and sums up all '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack() # calls each ability's attack value
        return total_damage # returns total attack power

    def add_armor(self, armor):
        '''Adds an armor to the armor list.'''
        self.armors.append(armor) # adds the armor to list
        print(f"{armor.name} has been added to {self.name}'s list")

    def defend(self):
        '''Loops through armors list and sums up all of block values.'''
        total_block = 0
        for armor in self.armors:
            total_block =+ armor.block() # counts block values
        return total_block # return total defense power
# runs examples
if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)            # Grace Hopper
    print(my_hero.current_health)  # 200

    my_hero1 = Hero("IronMan", 200) 
    print (my_hero1.name)
    print (my_hero1.current_health)

    my_hero1.battle(my_hero)
    greaseball = Ability("greaseball", 50)
    cheese = Ability("lactose intolerance", 40)
    peanut = Ability("peanut allergy", 55)
    my_hero.add_ability(greaseball)
    my_hero.add_ability(cheese)
    my_hero.add_ability(peanut)
    print(my_hero.sum_of_attacks())
    shield = Armor("Shield", 40)
    gloves = Armor("Gloves", 25)
    boots = Armor("Boots", 15)
    my_hero.add_armor(shield)
    my_hero.add_armor(gloves)
    my_hero.add_armor(boots)
    print(my_hero.defend())