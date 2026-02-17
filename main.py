import random
import art

c=1
while c==1:
    print(f"{art.logo}")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


    def deal_cards():
        n = random.choice(cards)
        return n


    def calculate_score(list_cards):
        if sum(list_cards) == 21 and len(list_cards) == 2:
            return 0

        if 11 in list_cards and sum(list_cards) > 21:
            list_cards.remove(11)
            list_cards.append(1)
        return sum(list_cards)


    def score_check(score):
        if score > 21:
            return 0


    # randomisation

    user_choice1 = deal_cards()
    user_choice2 = deal_cards()
    usercards = [user_choice1, user_choice2]
    userscore = calculate_score(usercards)

    computer_choice1 = deal_cards()
    computer_choice2 = deal_cards()
    computercards = [computer_choice1, computer_choice2]
    computerscore = calculate_score(computercards)

    print(f"user cards : {usercards[0], usercards[1]} , {userscore} ")
    print(f"computer cards : {computercards[0]}")

    if userscore == 0 or computerscore == 0:
        if userscore == 0:
            print(f"you have blackjack, you won")
        else:
            print(f"computer have blackjack, you lose")
    else:
        if score_check(userscore) != 0:
            chance = input("do you want a card,or to stand").lower()

            while chance != 'stand' and score_check(userscore) != 0:
                if chance == 'card':
                    usercards.append(deal_cards())
                    print(f"{usercards}")
                    userscore = calculate_score(usercards)
                    print(f"the sum of users card is {calculate_score(usercards)}")
                    if score_check(userscore) == 0:
                        print("you lose")

                if score_check(userscore) != 0:
                    chance = input("do you want a card,or to stand").lower()
            while chance == 'stand' and score_check(userscore) != 0:
                while computerscore < 17:
                    computercards.append(deal_cards())
                    print(f"computer cards after appending {computercards}")
                    computerscore = calculate_score(computercards)
                    print(f"the sum of computers card is {calculate_score(computercards)}")

                    if score_check(computerscore) == 0:
                        print("you won")
                    if userscore > computerscore:
                        print("you won")
                    elif userscore == computerscore:
                        print("draw")

                    else:
                        print("you lose")





        elif score_check(computerscore) == 0:
            print(f"computer has lose")

        else:
            print("you lose,greater than 21")

    restart=input("Do you want to restart this game ? yes or no").lower()
    if restart=='no':
        c=0