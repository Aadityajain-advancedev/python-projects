import random
import game_data
import art

print(art.logo)

def randomindex():
    return random.randint(1,51)-1




game_over=False
score=0

while game_over==False:
    a = randomindex()
    b= randomindex()
    while a == b:
        b = randomindex()
    print(f"Compare A : {game_data.data[a]["name"]},{game_data.data[a]["description"]},from {game_data.data[a]["country"]}")
    print(art.vs)
    print(f"Compare B: {game_data.data[b]["name"]},{game_data.data[b]["description"]},from {game_data.data[b]["country"]}")

    follower=input("Type A or B , who has more follower").lower()

    if follower=='a':
        if game_data.data[a]["follower_count"]> game_data.data[b]["follower_count"]:
            print("correct")
            score+=1
            print("\n" * 20)
            print(art.logo)
        else:
            print("incorrect")
            game_over=True
    elif follower=='b':
        if game_data.data[b]["follower_count"]> game_data.data[a]["follower_count"]:
            print("correct")
            score+=1
            print("\n" * 20)
            print(art.logo)
        else:
            print("incorrect")
            game_over=True

print(f"Your final score is {score}")
