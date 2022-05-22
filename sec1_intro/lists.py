# Lists

friends = ["Rolf", "Bob", "Anne"]

# access first element in friends
print(friends[0])

# grocery list
grocery = ["Milk", "Potato", "Bread", "Cereal"]

# make ANOTHER list through copying list
copy_grocery = grocery[:]
print(copy_grocery)

# two dimensional lists
student_scores = [
  ["Adam", 90], 
  ["Ali", 95],
  [ "Bob", 85], 
  ["Sarah", 86]                                          
]

# Accessing Ali and score
ali = student_scores[1][0]
ali_score = student_scores[1][1]

print(ali, ali_score)

# Adding item to an existing list
student_scores.append(["Emma", 94])
print(student_scores)

# removing items from lists
student_scores.remove(["Adam", 90])

print(student_scores, end="\n\n")

# list slicing
# [start, stop, step over]

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart)
print(amazon_cart[1:3])