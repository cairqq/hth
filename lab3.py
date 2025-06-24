# lab 3 

#task 1

food = "bun bo hue"
print(food[:3])
print(food[-3:])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)

#task 2 
number_list = [1, 3, 4, 54, -6, 0, 7689]
number_list.append(89)
print(number_list)
number_list.insert(3, 1000)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(number_list[1])
print(number_list)
print(number_list[:3])
print(number_list[-3:])

#task 3
books = {'stephen king': 'the shining', 'Dr. Seuss': 'Fox in Socks', 'J. K. Rowling': 'Harry Potter', 'Ray Bradbury':'Fahrenheit 451'}
print(books.keys())
print(books.values())
print(books.get('stephen king'))
books.pop(list(books.keys())[2])
print(books)
del books[list(books.keys())[0]]
print(books)