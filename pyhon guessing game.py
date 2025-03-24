import random
low=1
high=100
answer=random.randint(low,high)
guesses=0
is_running=True
print ("--------python number guessing game-------")
print(f"select number between {low} and {high}")

while is_running:

    guess=input("enter your guess:")

    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        
        if   guess<low  or guess > high:
            print(f"Out of range! Please select a number between {low} and {high}")
        elif guess< answer:
            print("Too low! try again")
        elif guess> answer:
            print("Too high! try again")
        else:
            print(f"correct anser is: {answer:10}")
            print(f"Number of guesses: {guesses:10}")
            is_running=False
            
    
    else:
        print("invalid guess")
        print(f"please select number between {low} and {high}")
input("\n Press Enter to exit.")
