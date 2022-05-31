"""
IF statement
  - if statement allows us to make decisions.
  - if statement
"""

friends = ["John", "Sarah", "Anna", "William"]
family = ["Mom", "Dad", "Leen", "Dina"]
user_name = input("Enter a name: ").title()

if  user_name in friends:
  print("Hello, friend!")
elif user_name in family:
  print("Hello, family member!")
else:
  print("Hello, stranger!")
  

print("")




