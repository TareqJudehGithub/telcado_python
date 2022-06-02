from unicodedata import name


print("")
friends = ["emad", "AJ", "yanal", "tamer"]

for friend in friends:
  print(friend)
  

print("")


# range()
# range(start, stop, step)

for i in range(1, 10, 2):
  print(i)
  
print("")  

students = [
  {"name": "Rolf", "grade": 85},
  {"name": "Sarah", "grade": 79},
  {"name": "Ali", "grade": 86},
  {"name": "Emma", "grade": 83}
]

# iterate over students, and assign variable name for each element
for student in students:
  name = student["name"]
  grade = student["grade"]
  print(f"{name.title()} scored {grade}" )