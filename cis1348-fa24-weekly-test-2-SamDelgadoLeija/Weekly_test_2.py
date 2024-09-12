"""Weekly Test 2"""
#Sam Delgado-Leija 1784791

# Sum of Even Numbers using a While Loop:
# Write a Python script to find the sum of all even numbers between 1 and 100 using a while loop.

initial_number = 2
sum_of_evens = 0

while initial_number <= 100:
    sum_of_evens += initial_number
    initial_number += 2

print("The sum of all even numbers between 1 and 100 is: ", sum_of_evens)