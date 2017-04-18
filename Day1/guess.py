# Author: Zhang Qing
oldboy_age=55
count = 0
for i in range(3):
 guess_age=int(input("guess age:"))
 if guess_age == oldboy_age:
    print("Bingo!")
    break
 elif guess_age < oldboy_age:
    print("Think older")
 else:
    print("Think yonger")
else:
    print("you have tried too many times!")