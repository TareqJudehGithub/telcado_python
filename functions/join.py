cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok"]
# count how many "ok" in cars list, and find the index of the last "ok" there.
cars_str = " ".join(cars)
last_ok = cars_str.rfind("ok")
count_ok = cars_str.count("ok")
print(len(cars_str), last_ok, count_ok)

