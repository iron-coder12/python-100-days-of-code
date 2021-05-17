print('''



                           ___
                          ( ((
                           ) ))
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `P `-;-`-`-`-`-`-`-`-`--| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    ) ((
                           ) ))
                          (_((


''')

print("Welcome to the Tresure Island")
print("Your mission is to find the treasure")

choice1 = input("Would you like to go Left(L) or Right(R)?")


if choice1 == str("L"):
    
    choice2 = input("You now have safly arrived at a lake.Do you want to make your own boat(B) or swim to the other side(S)?")

    if choice2 == str("B"):
        
      choice3 = input("You have safely reached the other side of the lake. You are now in front of the castle. Do you want to go inside the castle(I) or do you want to saty Outside(O)")
      
      if choice3 == str("I"):
         
         choice4 = input("you enter the castle and found two stairways. One leads up(U) the other down(D). On which Starecase do you want to go?")
          
         if choice4 == str("U"):
            
            
            print("The starecase you choose led to a room and you found the treasure. Congratulations!")
        
         else: 

            print("The starecase you choose led to a basement which had zombies in it and they killed you. GAME OVER")      
         
      else:
        print("Outside some zombies appeared and the killed you. GAME OVER")       
      
    else:
      print("You started swiming in the lake and got eaten by a crocodile. GAME OVER")    

else:
    print("That path leads to a cliff and fell and died!")
    
    
