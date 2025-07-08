menu = {'Pizza': 2.99,'Burger': 3.99,'Hot dog': 1.99,'Cheese': 0.59,'Ice cream': 1.49,'Churro': 0.79,'Soda': 0.89
}

def total_price(item1, item2):
    total_sum = menu[item1] + menu[item2]
    return total_sum

def price_difference(item1, item2):
    difference = abs(menu[item1] - menu[item2])
    return difference

def inflation(item, multiplier):
    menu[item] = menu[item] * multiplier
    return menu

def deflation(item, divisor):
    menu[item] = menu[item] / divisor
    return menu

def floor_discount(divisor):
    for item in menu:
        menu[item] = menu[item] // divisor
    return menu
print(total_price('Pizza', 'Burger'))
print(price_difference('Burger', 'Pizza'))
print(inflation('Pizza', 2))
print(deflation('Burger', 2))