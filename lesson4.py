'''Exercise 4: Shopping List Manager
Write a program that:

Creates a list called shopping_list with items: ["milk", "bread", "eggs"]
Asks the user to input an item they want to check
Uses a for loop to search through the shopping list
Prints "Already on the list!" if the item is found, "Need to add it!" if not found
'''


shopping_list = ["milk", "bread","eggs" ]
shopping_item = input("Enter the Item you want to check: ").lower()
found = False
'''for item in shopping_list:
     if shopping_item == item:
         found = True
         break
if found:
    print("Already on the list! ")
else:
    print("Need to add! ")'''
found = shopping_item in shopping_list
print(found)