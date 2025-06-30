checking = "yes"

while checking == "yes":
   print("whhat is your age")
   user_input = input()
   if int(user_input) >= 18:
        print ("yes you can vote")

   else: 
       print ("you can't vote")
   print("would you like to check another age?")
   user_input2 = input()
   checking = user_input2

list1 = [3,-1,0,6,-4]

for x in list1:
    if x > 0:
        print ("value is postive")
    elif x < 0:
        print("value is negative")
    else:
       print("value is zero")
    
inventory = ["tnt", "glass", "grass", "netherite", "waxed lightly weathered chisled copper stairs"]

for i in inventory:
    if i == "netherite":
        print(f"You found {i}! Congrats")
    else:
        print(f"You have {i}")