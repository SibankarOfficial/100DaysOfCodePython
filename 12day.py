# fruit = 1

# def change_fruit(fruit):
#     return fruit + 1
# print(change_fruit(fruit))
# print(fruit)

import random
print("Welcome to the Number Guissing Game!!")
print("I am thinking a number between 1 and 100.")
random_guess = random.randint(1, 100)
difficulty_level = input("Choose a difficulty - type 'easy' or 'hard' ")
attempts = 0 

if difficulty_level == "easy":
     attempts = 10
elif difficulty_level == 'hard':
     attempts = 5
print(f"You have total {attempts} attempts.")
def make_guess(attempts_no):
     guess_number = 0
     while attempts_no != 0 and guess_number != random_guess:
        guess_number = int(input("Guess a number: "))
        attempts_no -= 1
        if attempts_no == 0:
            print("Sorry, You dont have remaining attempts. ")
        elif guess_number == random_guess:
            print("Correct Guess! You Win.") 
        

        elif guess_number > random_guess:
            print(f"You have total {attempts_no} attempts.")
            print("Too high")
        else:
            print(f"You have total {attempts_no} attempts.")
            print( "Too low")      
        
 
make_guess(attempts)    






