print("Welcome to Python Pizza Deliveries!")
price=0
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size=="S":
    price=price+15
    if pepperoni == "Y":
        price += 2
    else:
        price += 0

elif size=="M":
    price+=20
    if pepperoni == "Y":
        price += 3
    else:
        price += 0
else:
    price+=25
    if pepperoni == "Y":
        price += 3
    else:
        price += 0



if extra_cheese=="Y":
    price+=1
else:
    price+=0

print(f"Your final bill is: ${price}.")