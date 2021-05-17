import random

print("printing a random number between 1 and 10")
random_integer = random.randint(1, 10)
print(random_integer)

#0.000000000 - 0.9999999999....
print("printing a float")
random_float = random.random() *5
print(random_float)

love_score = random.randint(1, 100)
print(f"your love score is {love_score}")

dice_roll = random.randint(1, 6)
print(f"You got a {dice_roll}")

input("_")