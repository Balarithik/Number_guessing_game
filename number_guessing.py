import random

rge=int(input("Enter thr range of numbers do wanna guess 1 to "))
num = random.randint(1,rge)

for i in range(1,(rge-1)):
    usr=int(input("Enter your number : "))
    if usr==num:
        print("You got it in ",i,"retakes")
        break
    else:
        print("Try agian your retakes ",i,'/',(rge-1))
if i<=(rge):
    print("You won this game ")
else :
    print("You lose this game ")
