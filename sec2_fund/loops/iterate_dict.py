from os import sep


friends = {
  "adam": 41, 
  "sarah": 38,
  "john": 45,
  "emma": 28
  }

# .keys()
for friend in friends.keys():
  print(friend, end=" | ")

# we could also iterate over dict keys by using:
for name in friends:
  print(name)
# That's correct—because the in keyword here checks if the contents of the 
# variable exist amongst the keys of the dictionary.


print("")  
# .values()
for age in friends.values():
  print(age, end=", ")

print("")  
# .items()
for friend, age in friends.items():
  print(f"{friend} is {age}.")

print("")
