print("")
empty_dic = dict()
friends = {
  "Rolf": 24,
  "Adam": 30,
  "Anne": 27
}

# print the first element value (for key "Rolf")
rolf_age = friends["Rolf"]

# Add new key and assign it a new value
bob = friends["Bob"] = 40

# Updates an existing key value:
friends["Rolf"] = 25

# tuples with dictionary element types in it

cars = (
  {"Brand": "BMW", "Year": 1997, "Model": 520},
  {"Brand": "Mercedes", "Year": 2021, "Model": 200},
  {"Brand": "GMC", "Year": 2006, "Model": "Envoy CLS"}
)

# Print the 3rd element Brand name
print(cars[2]["Brand"], end="\n\n")


# dict() function  ==> turns data into a dictionary
student_scores = [
  ("Bob", 79),
  ("Anna", 87),
  ("Sarah", 82),
  ("Ali", 91)
]
print(student_scores, end="\n\n")
# Convert student_scores into a dictionary
student_scores_dict = dict(student_scores)
print(student_scores_dict, end="\n\n")

