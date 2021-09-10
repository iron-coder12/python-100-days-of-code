#Write your code below this line 👇

def paint_calc(height, width, cover):
    print("Welcome to a program that calculates how muuch cans of paint you need to paint your wall.")
    print("It is quite simple")
    formula = "wall height ✖ wall Width ➗ coverage per can"
    print(f"Formula: {formula}")
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You will need {num_of_cans} cans of paint")








#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)