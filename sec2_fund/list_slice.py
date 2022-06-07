# Slicing getting a part of a list or an iterable.
from audioop import reverse


print("")

grocery = ["bread", "milk", "cereal", "orange juice", "tomatoes", "orange"]
print("")

# get me the first three items in grocery
print(grocery[:3])
# or grocery[0:3]
print("")

# get me the 3rd, 4th, and 5th items
print(grocery[2:5])
print("")

# get me the last three items starting from the end
print()
print("")
last_three = grocery[-3:]
last_three.reverse()
print(last_three)


print("")
# reverse grocery using list slicing
print(grocery[::-1])

print("")