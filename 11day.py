#backjack game
#game start --> deal card --> 2 cards for user and 2 cards for dealer --> player
# can see 1 card of dealer and his both card --> player total card > dealer total == player win 
# if not dealer win, now player can take 1 more card or want to see dealer last card, if player want 1 more card then 1 more card will be 
# distributed from the deck and if total > 21 then player lose, dealer card not matter, if player want to see dealer card then 
# dealer last card will be open, if dealer total < 15 then 1 more card will be distributed from the deck 
# if dealer total == player total then match draw
# ace is calculated as 11, if total > 21 , then ace calculated as 1, 10, jack, queen, king, these 4 cards calculated as 10



import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(deck_of_card):
    card = random.choice(deck_of_card)
    return card
def calculate_score(cards):
     if sum(cards) == 21 and len(cards) == 2:
        return 0    
     if 11 in cards and sum(cards) > 21:
          cards.remove(11)
          cards.append(1)

     return sum(cards) 






def compare_score(u_score, c_score):
    if u_score == c_score:
         return "Draw"
    elif u_score == 0:
        return " You have a black jack, You won"
    elif c_score == 0:
        return "computer has a black jack, You lose"
    elif c_score> 21:
         return("Computer went over, You won")
    elif u_score>21:
         return("You went over, you lose")
    elif c_score > u_score and u_score != 0:
            return "You Lose"
    elif u_score > c_score and c_score != 0:
            return "You Won"
def play_blackjack():    
    user_cards = []
    dealer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False
    def distribute_card():
        for i in range(2):
            user_cards.append(deal_card(cards))
            dealer_cards.append(deal_card(cards))

    distribute_card()


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(dealer_cards)
        print(f"Your card is {user_cards}, score {user_score}")
        print(f"Dealer 1st card is {dealer_cards}, score {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True 
        else:
            is_hit = input("Dou you want to take 1 more card? type 'yes' or 'no' \n").lower()

            if is_hit == "yes":
                new_card = deal_card(cards)
                user_cards.append(new_card)
            elif is_hit == "no":
                is_game_over = True 


    while computer_score != 0 and computer_score < 17:
        dealer_cards.append(deal_card(cards))
        computer_score = calculate_score(dealer_cards)
        print(f"new computer cards {dealer_cards} and score {computer_score}")


    print(compare_score(user_score, computer_score))

if input("do you want to play BlackJack? type 'y' for yeas and 'n' for no ") == "y":
     print("\n" * 20)
     play_blackjack()

    


















