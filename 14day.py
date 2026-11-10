
import random
import game_data



logo = """    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """ _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

#todos - 1. logo initialise
#2. generate 2 random item from list, person a and b, print both for user
#3. compare the followers of these 2 items
#4. user guess input higheir or lower
#5. conditional statement on user input in loop
#6. score update
#7. final score update and loop break

def formate_data(person):
    person_name = person['name']
    person_desc = person['description']
    person_country = person['country']
    person_follower = person['follower_count']
    return f"{person_name}, {person_desc}, from {person_country}."

print(logo)





game_over = False
user_score = 0
def compare_followers(guess,a_follower,b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


person_b = random.choice(game_data.data)

while not game_over:   
    person_a = person_b
    person_a_followers = person_a["follower_count"]
    person_b = random.choice(game_data.data)
    if person_a == person_b:
        person_b = random.choice(game_data.data)
    person_b_followers = person_b["follower_count"] 
    print(f"Compare A: {formate_data(person_a)}")
    print(vs)
    print(f"Compare B: {formate_data(person_b)}")






    user_guess = input("Who has more followers? Type 'A' or 'B'").lower()

    #clear screen
    print("\n" *20)
    print(logo)

    is_correct = compare_followers(user_guess, person_a_followers, person_b_followers)

    if is_correct:
        user_score += 1
        print(f"You are correct, your score is {user_score}")
    else:
        print(f"Sorry, that's wrong, your final score {user_score}")
        game_over = True


    
    

     








