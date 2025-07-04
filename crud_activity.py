# As a baker i want a program that can cread read update and delete

cookbook = []

def create(recipe):
    cookbook.append(recipe)
    print(f"The recipe {recipe} has been added")

def read(index):
    if 0 <= index < len(cookbook):
        return cookbook[index]
    else:
        print("PLEASE PICK AN INDEX WITHIN THE RANGE")
        
def update(index, recipe):
    if 0 <= index < len(cookbook):
        old_recipe = cookbook[index]
        cookbook[index] = recipe
        print(f"The recipe at index {index} has been updated from '{old_recipe}' to '{recipe}'.")
    else:
        print("Please pick an index within the range.")

def destroy(index):
    if 0 <= index < len(cookbook):
        removed_recipe = cookbook.pop(index)
        print(f"The recipe '{removed_recipe}' has been removed.")
    else:
        print("Please pick an index within the range.")

def list_all_recipes():
    if cookbook:
        print("Current recipes in the cookbook:")
        for i, recipe in enumerate(cookbook):
            print(f"{i}: {recipe}")
    else:
        print("The cookbook is currently empty.")

while True:
    print("\n--- Cookbook Menu ---")
    print("1. Add a recipe")
    print("2. Read a recipe by index")
    print("3. Update a recipe by index")
    print("4. Delete a recipe by index")
    print("5. List all recipes")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        recipe = input("Enter the recipe name: ")
        create(recipe)
    elif choice == "2":
        index = int(input("Enter the index to read: "))
        result = read(index)
        if result:
            print(f"Recipe at index {index}: {result}")
    elif choice == "3":
        index = int(input("Enter the index to update: "))
        recipe = input("Enter the new recipe: ")
        update(index, recipe)
    elif choice == "4":
        index = int(input("Enter the index to delete: "))
        destroy(index)
    elif choice == "5":
        list_all_recipes()
    elif choice == "6":
        print("Exiting the cookbook. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")