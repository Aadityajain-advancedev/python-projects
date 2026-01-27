logo="""    __   ___   _____  _____  ___    ___      ___ ___   ____    __  __ __  ____  ____      
           /  ] /   \ |     ||     |/  _]  /  _]    |   |   | /    |  /  ]|  |  ||    ||    \   /  _]
          /  / |     ||   __||   __/  [_  /  [_     | _   _ ||  o  | /  / |  |  | |  | |  _  | /  [_ 
         /  /  |  O  ||  |_  |  |_|    _]|    _]    |  \_/  ||     |/  /  |  _  | |  | |  |  ||    _]
        /   \_ |     ||   _] |   _]   [_ |   [_     |   |   ||  _  /   \_ |  |  | |  | |  |  ||   [_ 
        \     ||     ||  |   |  | |     ||     |    |   |   ||  |  \     ||  |  | |  | |  |  ||     |
         \____| \___/ |__|   |__| |_____||_____|    |___|___||__|__|\____||__|__||____||__|__||_____|
                                                                                                      
          """
print(logo)






MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def transaction(coffename):

    actualcost=MENU[f"{coffename}"]["cost"]
    print("please insert coins ")
    q=int(input("how many quarters?"))
    d=int(input("how many dimes?"))
    n=int(input("how many nickles?"))
    p=int(input("how many pennies?"))
    total_coins_inserted=q*0.25+d*0.1+n*0.05+p*0.01

    if actualcost==round(total_coins_inserted,2):
        print("transaction is successful")
        resources_list(coffename)

    elif round(total_coins_inserted, 2)>actualcost:
        change=round(total_coins_inserted-actualcost,2)
        print(f"Here is ${change} in change")
        resources_list(coffename)
    else:
        print("Sorry that's not enough money. Money refunded.")

def resources_list(coffename):

    water=MENU[f"{coffename}"]["ingredients"]["water"]
    milk=MENU[f"{coffename}"]["ingredients"].get("milk", 0)
    coffee=MENU[f"{coffename}"]["ingredients"]["coffee"]


    water_initial=resources["water"]
    milk_initial = resources["milk"]
    coffee_initial = resources["coffee"]

    if water_initial>=water and milk_initial>=milk  and coffee_initial>=coffee:
        resources["water"] -= water

        resources["milk"] -= milk
        resources["coffee"] -= coffee
        print(f"the {coffename} is being ready for you")
    else:
        Needed_list=[]
        if water_initial<water:
            Needed_list.append("water")
        if milk_initial<milk:
            Needed_list.append("milk")
        if  coffee_initial<coffee:
            Needed_list.append("coffee")
        print(f"Things to be needed for making you a {coffename} : {Needed_list}")
        print(f"the money is refunded")





coffename="on"
while coffename!='off':
    coffename = input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffename=='report':
            print(f"water left : {resources["water"]}")
            print(f"milk left : {resources["milk"]}")
            print(f"coffee left : {resources["coffee"]}")
    else:
        transaction(coffename)