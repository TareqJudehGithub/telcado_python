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

print("")  
# .values()
for age in friends.values():
  print(age, end=", ")

print("")  
# .items()
for friend, age in friends.items():
  print(f"{friend} is {age}.")

