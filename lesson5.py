'''Exercise 5: Even Number Counter
Write a program that:

Asks the user how many numbers they want to enter
Creates an empty list called numbers
Uses a for loop to get that many numbers from the user and add them to the list
Uses another for loop to count how many even numbers are in the list
Prints the total count of even numbers'''

numbers = []
question = input ("How many numbers do you want to enter? ")
for _ in range(int(question)):
    number = input("enter a number ")
    numbers.append(number)
evens = 0
for number in numbers:
    if int( number) % 2 == 0:
        evens += 1
print(numbers)
print(evens)