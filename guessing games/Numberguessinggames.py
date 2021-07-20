import random
import time


guess=0
tries=0
number= random.randint(1,10)

name= input("Hi, May I Know Your Name? ")
print(f"hello, {name.upper()}.")

question= input("Are You Ready To Guess? [Y/N]")
time.sleep(1)

if question.lower()=="n":
    print("I'm sorry, We'll meet some other time!")
    exit()
if question.lower()=="y":
    print("I'm thinking of a number between 1 & 10")
    
while not(guess==number):
    time.sleep(1)
    guess= int(input("whats your guess? "))
    tries= tries+1
    if (guess==number):
        print("Brilliant")
        time.sleep(1)
        print("Congrats, Your Guess was Correct. The number was indeed {}.".format(number))
        time.sleep(1)
        print("It has taken you {} tries.".format(tries))
    elif(guess<number):
        time.sleep(1)
        print("No, Guess higher!")
    elif(guess>number):
        time.sleep(1)
        print("No, Guess lower!")  


