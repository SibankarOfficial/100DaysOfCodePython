# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.



# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.



# It will take your current age as the input and output a message with our time left in this format:



# You have x weeks left.



# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

# current_age = int(input("Enter your age"))

# def life_in_weeks(current_age):
#     weeks_left = (90 - current_age)*52
#     print(f"you have {weeks_left} left.")

# life_in_weeks(current_age)



# def greet_with(name, location):
#     print(f"hello {name}, how is the weather at {location}")

# #positional arguments, default position same as parameter
# greet_with("raju","kolkata")

# # keyword arguments, argument associated with keywords so position dosnt matter anymore
# greet_with(location="kolkata",name="sibankar")



# 💪 This is a difficult challenge! 💪 

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

# 2. Then check for the number of times the letters in the word LOVE occurs.   

# 3. Then combine these numbers to make a 2 digit number and print it out. 

# e.g.

# name1 = "Angela Yu" name2 = "Jack Bauer"

# T occurs 0 times 

# R occurs 1 time 

# U occurs 2 times 

# E occurs 2 times 

# Total = 5 

# L occurs 1 time 

# O occurs 0 times 

# V occurs 0 times 

# E occurs 2 times 

# Total = 3 



# Love Score = 53





# Example Input 

# calculate_love_score("Kanye West", "Kim Kardashian")

# Example Output

# 42

# def calculate_love_score(name1, name2):
#     concatinate_name = (name1+name2).lower()
#     # true_count = 0
#     # love_count = 0
#     # for letter in concatinate_name:
#     #     if letter == "t":
#     #         true_count += 1
#     #     elif letter == "r":
#     #         true_count += 1
#     #     elif letter == "u":
#     #         true_count += 1
#     #     elif letter == "e":
#     #         true_count += 1

#     # for letter in concatinate_name:
#     #         if letter == "l" or letter == "o" or letter == "v" or letter== "e":
#     #             love_count += 1
#     #By using count function
#     t = concatinate_name.count("t")
#     r = concatinate_name.count("r")
#     u = concatinate_name.count("u")
#     e = concatinate_name.count("e")

#     true_count = t+r+u+e


#     l = concatinate_name.count("l")
#     o = concatinate_name.count("o")
#     v = concatinate_name.count("v")
#     e = concatinate_name.count("e")
#     love_count = l+o+v+e

#     score = str(true_count) + str(love_count)
#     print(score)

# calculate_love_score("Kanye West","Kim Kardashian")



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(alphabet.index('z'))

def encrypt(original_text, shift_amount):
    encrypt_word = ""
    for letter in original_text:
        if letter == " ":
            encrypt_word += " "
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            if shifted_position>26:
                shifted_position -= 26

            encrypt_word += alphabet[shifted_position]

        
    print(encrypt_word)

def decrypt(original_text, shift_amount):
    decrypt_word = ""
    for letter in original_text:
        if letter == " ":
            decrypt_word += " "
        else:
            shifted_position = alphabet.index(letter) - shift_amount
            if shifted_position<0:
                shifted_position += 26
                
            decrypt_word += alphabet[shifted_position]

        
    print(decrypt_word)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))
if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print("Please type 'encode' to encrypt, type 'decode' to decrypt")
