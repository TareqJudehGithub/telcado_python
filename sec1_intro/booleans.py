print("")
age = 20

is_over_age = "You're old enough"
is_under_age = "Come back in a few more years"

# ask user for an age number:
my_age = int(input("Enter your age: "))
can_learn_coding = my_age >= 15 and my_age < 80
if my_age >= 15:
  print(is_over_age)
  print(can_learn_coding, "You can learn programming")
else:
  print(is_under_age, )
  print(can_learn_coding, "Sorry, you can't learn programming!")
  
  

print("\n")

is_working = my_age >= 18 and my_age <= 64

print(f"At the age of {my_age}, you're usually working: {is_working}")
if is_working:
  print("You're Working")
else:
  print("Not working")
  
print("\nbool built-in function:")

print(bool(0))


# and, or, not

# and returns True if all expressions were true
print("\nand operator")
print("15 > 20 and 5 >= 5", 15 > 20 and 5 >= 5)

# or returns True if one of the expressions is true
print("\nor operator")
print("15 > 20 or 5 >= 5", 15 < 20 or 5 > 5)

# not Reverse the result, returns False if the result is true
print("\nnot operator")
print("not 10 > 5", not 10 > 5, end="\n\n")

x = True
cmp = x and 18
print(cmp)