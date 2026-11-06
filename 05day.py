# numbers = [12,443,5764,23,65,24,324,46,234]

# #sum = sum(numbers)
# #max_number = max(numbers)
# sum = 0
# max_number = 0

# for number in numbers:
#     if number > max_number:
#         max_number = number


# sum = 0

# for number in range(1,101):
#     sum += number

# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:



# Your program should print each number from 1 to 100 in turn and include number 100.



# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".



# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`



# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"



# for number in range(1,101):
#     if number % 3 == 0 and number % 5==0:
#         print("FizzBuzz")
    
#     elif number % 3 == 0:
#             print("Fizz")
#     elif number % 5 ==0:
#             print("Buzz")
#     else:
#           print(number)


import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

numbers = [
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9'
]

symbols = [
    '!', '#', '$', '%', '&',
    '(', ')', '*', '+'
]

total_char = int(input("How many characters whould you like in your password? \n"))
total_symbols = int(input("How many symbols?\n"))
total_numbers = int(input("How many numbers?\n"))

# password = ""



#easy level

# for char in range(0, total_char):
#     random_char = random.choice(letters)
#     password += random_char

# for number in range(0, total_numbers):
#     random_num = random.choice(numbers)
#     password += random_num

# for symbol in range(0, total_symbols):
#     random_symbol = random.choice(symbols)
#     password += random_symbol

# # random_index = random.random()


# print(password)

password = []

for char in range(0, total_char):
    random_char = random.choice(letters)
    password.append(random_char)

for number in range(0, total_numbers):
    random_num = random.choice(numbers)
    password.append(random_num) 

for symbol in range(0, total_symbols):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)

final_pass = ''
## random.shuffle() dosnt return a new list, it only shuffle the items position of the list,
## so dont assign new var to suffle list, u can access with previous variable itself
random.shuffle(password)

for char in password:
    final_pass += char



print(final_pass)


