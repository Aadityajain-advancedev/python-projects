girl=input("What is your name?").lower()
boy=input("What is your boyfriend name?").lower()


def calculate_love_score(name1,name2):
    char1=['t','r','u','e']
    score1 = 0
    for letter in name1:
        if letter in char1:
            score1+=1
    score2 = 0
    for letters in name2:
        if letters in char1:
            score2+=1
    true=score1+score2



    char2=['l','o','v','e']
    score3=0
    for let in name1:
        if let in char2:
            score3+=1

    score4=0
    for lett in name2:
        if lett in char2:
            score4+=1

    love=score3+score4

    print(f"Your love score is {true}{love}")
calculate_love_score(girl,boy)