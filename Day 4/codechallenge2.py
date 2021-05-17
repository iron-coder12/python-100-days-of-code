import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_iteams = len(names)
random = random.randint(0, num_iteams - 1)
print(random)
person = names[random]

print(person + " will be paying the bill today")


