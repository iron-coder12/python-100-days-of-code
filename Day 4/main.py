import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
       (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
            ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock paper scissors game!")
game_images = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for rock 1 for paper and 2 for Scissors.\n"))

if player_choice >= 3 or player_choice <0:
    print("ah you just typed an invalid number which means you lose 👎")  

else:
    print(game_images[UserWarning])


print(game_images[player_choice])
computer_choice = random.randint(0, 2)
print("computer chose: ")
print(game_images[computer_choice])


if player_choice == 0 and computer_choice == 2 :
    print("You my young man just won 🎉")
elif computer_choice == 0 and player_choice == 2:
    print("You win! 🎉") 
elif computer_choice > player_choice:
    print("You young man lost. Loser! 👎")
elif computer_choice > player_choice:
    print("You won!")    
elif computer_choice == player_choice:
    print("It's a draw 🤝")    


