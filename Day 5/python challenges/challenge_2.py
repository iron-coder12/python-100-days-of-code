# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#INPUT TO BE GIVEN - 78 65 89 86 55 91 64 89
highest_score = 0
for scores in student_scores:
    if scores > highest_score:
        highest_score = scores
print(f"the highest score is {highest_score}")        