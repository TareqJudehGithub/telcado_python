from itertools import count

cars = ["ok", "ok", "ok", "ok", "bad", "ok", "ok"]

for status in cars:
  if status is not "ok":
    print(f"This car status is {status}")
    break
  else:
    print(f"This car status is {status}")
# we can also use 'else' with loops. 
else:
  print("end of loop")  

print("")


