# List Comprehension with conditionals.

# extract the odd ages from ages list into a new list

ages = [55, 46, 42, 35, 34, 29]

odd_ages = [f"{age} is odd" for age in ages if age % 2 != 0]
print(odd_ages, end="\n\n")

# combine both friends and guests list into a new list called
# new_friends using list comprehension
friends = ["emma", "sarah", "julie", "adams", "jose"]
guests = ["julie", "micheal", "rolf", "jose"]
new_friends = list()

# for friend in friends:
#   if friend.title() not in new_friends:
#     new_friends.append(friend.title())

# for guest in guests:
#   if guest.title() not in new_friends:
#     new_friends.append(guest.title())

# print(new_friends, end="\n\n")

friends_comp = [
  friend.title() 
  for friend in guests 
  if friend in friends
]
print(friends_comp)
