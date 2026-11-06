import random
word_list = ["mouse", "pen", "wife","camel","egg","banana"]
stages = [
    # 6 mistakes (full body - game over)
        r"""
         +---+
         O   |
        /|\  |
        / \  |
           ===""",
    # 5 mistakes (head + torso + both arms + one leg)
        r"""
         +---+
         O   |
        /|\  |
        /    |
           ===""",
    # 4 mistakes (head + torso + both arms)
        r"""
         +---+
         O   |
        /|\  |
             |
           ===""",
    # 3 mistakes (head + torso + one arm)
        r"""
         +---+
         O   |
        /|   |
             |
           ===""",
    # 2 mistakes (head + torso)
        r"""
         +---+
         O   |
    
         |   |
             |
           ===""",
    # 1 mistake (head)
        r"""
         +---+
         O   |
             |
             |
           ===""",        
    # 0 mistakes (empty gallows)
    r"""
     +---+
         |
         |
         |
       ==="""
    
]


# random_word = word_list[random.randint(0,(len(word_list)-1))]
random_word = random.choice(word_list)

# print(random_word)

len_of_word = len(random_word)
blank = ""

for item in range(len_of_word):
    blank += "_"

print(blank)

game_over = False
correct_letters = []
lives = 6
while not game_over:
    guess_letter = input("Enter a letter: ").lower()
    display = ""
    
     
    for letter in random_word:
        if letter == guess_letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess_letter not in random_word:
            lives -= 1
            
            if lives == 0:
                 game_over = True
                 print("You Lose")
    
    print(stages[lives])      
    if "_" not in display:
        game_over = True
        print("You Won!!")
    

    

