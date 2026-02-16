"""Sum of Even Numbers
Write a function that takes a list of numbers and returns the sum of all even numbers using a for loop"""

numbers = []
question = input("How many numbers do you want enter?")
for _ in range(int(question)):
    number = input("Enter a number")
    numbers.append(number)
evens = 0
for number in numbers:
    if int (number) % 2 == 0:
        evens += 1
print(numbers)
print(evens)
