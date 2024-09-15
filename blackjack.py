import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def condition_check(user_cards_sum, comp_cards_sum, user_cards, comp_cards):
    if user_cards_sum > comp_cards_sum:
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")

        print("You win 😃")
    elif user_cards_sum == comp_cards_sum:
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")

        print("Draw 😐")
    else:
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")

        print("You lose 😭")


def blackjack_condition(user_cards, comp_cards):
    if (10 in user_cards and 11 in user_cards) and (10 in comp_cards and 11 in comp_cards):
        print("You lose! Computer gets a blackjack! (Draw Condition)")
        return True
    elif 10 in user_cards and 11 in user_cards:
        print("You win! Blackjack!")
        return True
    elif 10 in comp_cards and 11 in comp_cards:
        print("You lose! Computer gets a blackjack!")
        return True
    else:
        return False


def blackjack_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    comp_cards = []
    for i in range(2):
        user_cards.append(random.choice(cards))
        comp_cards.append(random.choice(cards))

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")

    # Blackjack Condition Check
    while sum(user_cards) <= 21 and sum(comp_cards) <= 21 and not blackjack_condition(user_cards, comp_cards):
        draw_or_pass = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if draw_or_pass == 'n':
            while sum(comp_cards) <= 16:
                comp_cards.append(random.choice(cards))
            if sum(comp_cards) > 21:
                # Ace Condition
                if 11 in comp_cards:
                    comp_cards.pop(comp_cards.index(11))
                    comp_cards.append(1)
                    condition_check(sum(user_cards), sum(comp_cards), user_cards, comp_cards)
                    break
                else:
                    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
                    print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
                    print("You win!")
            else:
                condition_check(sum(user_cards), sum(comp_cards), user_cards, comp_cards)
                break
        else:
            user_cards.append(random.choice(cards))
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"Computer's first card: {comp_cards[0]}")

            if sum(user_cards) > 21:
                # Ace Condition
                if 11 in user_cards:
                    user_cards.pop(user_cards.index(11))
                    user_cards.append(1)
                    condition_check(sum(user_cards), sum(comp_cards), user_cards, comp_cards)
                    break
                else:
                    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
                    print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
                    print("You lose!")


game_over = False
while not game_over:
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if want_to_play == 'y':
        print(logo)
        blackjack_game()
    else:
        print("Good Bye!")
        game_over = True



