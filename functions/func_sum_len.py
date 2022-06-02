# print() - prints Python output to the console
print("Hello, world!", end="\n\n")

# sum() 
# - adds sum of a given list elements

# len() 
# - calculates the number of total items in an object
# len only works on a "sequence (such as a string, bytes, tuple, list, or range) or a 
# collection (such as a dictionary, set, or frozen set)
grades = [80, 75, 81, 94, 67, 75]

# Calculate the average score for grades list

average = sum(grades) / len(grades)
print(round(average), end="\n\n")

# round() rounds a float value to the nearest integer.

# type() 
# type() function it can be used to check the data type of any variable you are
# working with.