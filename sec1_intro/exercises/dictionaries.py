lottery_numbers = {13, 21, 22, 5, 8}

"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

players = [
  {
    "name": "Sarah", 
    "numbers": {21, 100, 1, 3, 8}
    },
  {
    "name": "Adam",
    "numbers": {32, 13, 5, 1, 21}
    }
]

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 
numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they 
matched with lottery_numbers.You'll have to access each player's name and numbers, and 
calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got
right!
"""
player1_name = players[0]["name"]
player1_numbers = players[0]["numbers"]

player1_winning_numbers = lottery_numbers.intersection(player1_numbers)
player1_wins_total = len(player1_winning_numbers)
print(f"Player {player1_name} got {player1_wins_total} numbers right.")

player2_name = players[1]["name"]
player2_numbers = players[1]["numbers"]
player2_winning_numbers = lottery_numbers.intersection(player2_numbers)
player2_wins_total = len(player2_winning_numbers)
print(f"Player {player2_name} got {player2_wins_total} numbers right.")


elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

"""
Quiz: Adding Values to Nested Dictionaries
todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
hint: helium is a noble gas, hydrogen isn't
"""
elements["hydrogen"]["is_noble_gas"] = False
elements["helium"]["is_noble_gas"] = True


print("")

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(set(verse_dict.keys()))
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict.keys()
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())


# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(max(sorted_keys)) 
