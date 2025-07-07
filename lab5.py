# lab 5 carina bui

# step 1

def cat_greeting(word):
    print(f'cat says {word}')

cat_greeting('meow')

# step 2

def generate_superhero_power1():
    name = "Kitty"
    power = "mind reading"
    print (f"{name}'s power is {power}")

generate_superhero_power1()

# step 3

def generate_superhero_power2():
    power = "mind reading"
    return power

print(generate_superhero_power2())

# step 4 

def generate_superhero_power3(user_name, super_power):
    message = user_name + " has the power of " + super_power + " !"
    return message

print(generate_superhero_power3("doggy", "fire breathing"))

# step 5
def cat_greetings_loop(greeting):
    for i in range(5):
        print(f'The cat says {greeting}')

cat_greetings_loop("meow")

# step 6 
def generate_multiple_powers(powers):
    for power in powers:
        print(power)

generate_multiple_powers(["super eating", "rainbow farts", "egg cannon"])


