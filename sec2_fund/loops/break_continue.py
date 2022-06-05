from itertools import count


cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
  if status == "faulty":
    print(f"This car status is {status}")
    continue
  else:
    print(f"This car status is {status}")
print("end of loop")
print("")


