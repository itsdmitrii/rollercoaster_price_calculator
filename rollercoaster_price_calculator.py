higth = int(input("What is you higth in cm?\n"))

if higth >= 120:
  print("Yey! You can ride the rollercoaster!")
  age = int(input("What is your age? \n"))
  if age <= 12:
    bill = 5
    print(f"You pay child price ${bill}")
  elif age <= 18:
    bill = 7
    print(f"You pay youth price ${bill}")
  else:
    bill = 12
    print(f"You pay adult price ${bill}")
    
  wants_photo = input("Dou you want photo? Y or N\n")
  if wants_photo == "Y":
    bill += 3
    print(f"Your total price is ${bill} ")
    
else:
  print("You can't ride")