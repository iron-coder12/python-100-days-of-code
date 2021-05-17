print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# > Greater Than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to


if height >= 100:
    print("you can ride the rollarcoaster!")
    age = int(input("What is your age?"))
    if age < 12:
      print("please pay $5")
    elif age<=18:
      pass
    else:
      print("The cost of tickets will be $12")
else:
    print("grow up tall first")
