my_string = "Hello, world!"
print(my_string)

multiple_quotations = "My name's Tareq. This is Tareq's car"
print(multiple_quotations)


multiline_string = """
Hello,
  My name's John Smith!
"""
print(multiline_string)
# Python DocStrings """"""  used in functions to describe it


# String concatenation
# Python does not support concatenation between different types.
name = "John"
print("Hello, " + name)

# String formatting in Python

# 1. f string  - available in python 3.6+
print(f"Hey, {name}")

# 2. .format()
time_day = "morning"
print("Good {}, {}".format(time_day, name))

