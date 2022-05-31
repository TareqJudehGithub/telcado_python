is_learning= True

while is_learning:
  print("You're still learning!")
  is_learning = input("Are you still learning? (y/n) ").lower()
  
  if is_learning == 'y':
    continue
  else:
    print("Congratulations!")
    break
  