from locale import currency


# Destructing takes a tuple, turning it into multiple variables.
x, y, z = 1, 2, 3

print(x, y, z)

print("")

currencies = 0.8, 1.5

usd, eur = currencies

print(usd, eur)

print("")

friends = [
  ("adam", 41), 
  ("sarah", 38),
  ("john", 45),
  ("emma", 28)
  ]

# iterate over all iterables and destruct them into two variables
for name, age in friends:
  print(f"{name} is {age} years old.")

