import random

# random_num = random.randint(0,4)

# friends = ["raju", "ruma", "siba", "krisna", "ganesh"]
# print(friends[random_num])

# #or use choice
# print(random.choice(friends))

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

s_p_s = [rock, paper, scissors]
# user_input = s_p_s[int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors"))]
# print(user_input)

# computer_input = random.choice(s_p_s)
# print(computer_input)

# if user_input == rock and computer_input == paper:
#     print("You loose")
# elif user_input == rock and computer_input == scissors:
#     print("You Won")
# elif user_input == paper and computer_input == scissors:
#     print("You loose")
# elif user_input == paper and computer_input == rock:
#     print("You Won")
# elif user_input == scissors and computer_input == paper:
#     print("You Won")
# elif user_input == scissors and computer_input == rock:
#     print("You loose")
# else:
#     print("Try again!!")


user_input = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors\n"))
if user_input <= 2 and user_input >=0:
    print(s_p_s[user_input])

computer_input = random.randint(0,2)
print(f"computer choose:\n {s_p_s[computer_input]}")



#how many conditions can be possible
if user_input <= 2 and user_input >=0:
    if user_input == 0 and computer_input== 2:
                    print("You won")
    elif user_input == 2 and computer_input == 0:
         print("You lose")
    elif user_input < computer_input:
        print("You lose")
    
    elif user_input > computer_input:
            print("You won")
    
    else:
           print("Try again, match draw!")
else:
    print("Enter a valid number.")

