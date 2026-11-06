# print("wlecome rollercoaster")
# height = int(input("what is your height?"))
# bill = 0

# if height > 120:
#     age = int(input("what is your age?"))
#     if age < 12:
#         bill = 5
#     elif age < 18:
#         bill = 8
#     elif age >= 45 and age <= 55:
#         bill = 0
#     else:
#         bill = 12
#     want_photo = input("Do you want a photo? y for yes and n for no")
#     if want_photo == "y":
#         if 45 <= age <= 55:
#              bill = 0
#         else:
#             bill += 3

#     print(f"please pay ${bill}")
# else:
#     print("go home") 

# number = int(input("type a number"))
# if number % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

#BMI Calculator
# print("BMI Calculator")
# height = float(input("Whats your height(in cm)? "))/100
# weight = float(input("Whats your weight(in kg)? "))

# bmi = weight / height **2

# if bmi < 18.5:
#     print("under weight")
# elif bmi < 24.9:
#     print("normal")
# else:
#     print("over weight")

#Pizza delivery
# print("welcome to sibankar pizza delivery")
# size = input("What sizw yu want to order? S, M or L \n")
# peparonni = input("do you want paparonni? Y oe N\n")
# extra_chease = input("do you want extra chease? Y or N\n")
# bill = 0

# if size == "S":
#         bill += 15
# elif size == "M":
#         bill += 20
# elif size == "L":
#         bill += 25
# else:
#     print("Wrong input, please type S, M or L")

# if peparonni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#           bill += 3


# if extra_chease == "Y":
#     bill += 1
# print(f"Your total bill ${bill}.")

#final project 
print("Welcome to Treasure Island. Your mission is to find the treasure.")
direction = input("where do you want to go?\nType 'left' or 'right'\n")





if direction == "left":
    action = input("What do you want to do?\nyou can 'wait' or 'swim'\n")
    
    if action == "wait":
        door = input("Which door you want to open?\nthere are 3 doors, red , yellow and blue\n")
        if door == "yellow":
            print("Congo, You Win..")
        elif door =="red":
            print("Burned by fire.Game Over.")
        else:
            print("Eaten by beasts. Game Over.")


    else:
        print("Attacked by trout. Game over")

else:
    print("Fall into a hole. Game Over.")