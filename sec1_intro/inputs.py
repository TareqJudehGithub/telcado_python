"""
Inputs in Python

"""


my_name = "john smith".title()

# Ask user of his/her name
your_name = input("What is your name? ").title()

# Convert str to int
your_age = int(input("What is your age? "))

# output
print(f"Hello, my name is {my_name}, nice to meet you, {your_name}!\n\
      You are {your_age // 3} years old.", end="\n\n")