""" 
while loop
while loop allows us to repeat a block of code for as long as a condition is 
True.
# That's right! As soon as the condition becomes False, the loop stops 
# repeating.
is_learning= True

"""
while is_learning:
  print("You're still learning!")
  is_learning = input("Are you still learning? (y/n) ").lower()
  
  if is_learning == 'y':
    continue
  else:
    print("Congratulations!")
    break
  