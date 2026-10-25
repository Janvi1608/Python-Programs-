import random 
import time
choice = "rock" , "paper" , "scissors"  
comp=random.choice(choice)
user=str(input("enter choice : (rock , paper , scissors"))
time.sleep(2)
print("Computer chooses",comp)
time.sleep(2)
if comp==user:
    print("DRAW")
elif comp=="rock" and user=="paper":
    print("USER WINS")
elif comp=="rock"and user=="scissors":
    print("COMPUTER WINS")
elif comp=="paper"and user=="scissors":
    print("USER WINS")
elif comp=="paper" and user=="rock":
    print("COMPUTER WINS")
elif comp=="scissors" and user=="rock":
    print("USER WINS") 
elif comp=="scissors" and user=="paper":
    print("COMPUTER WINS")
else:
    print("invalid choice")
