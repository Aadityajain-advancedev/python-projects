print(r'''

                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction=input("which direction you want to choose : 'left' or 'right'")



if direction=="left"or"Left":
    print("excellent choice:")
    aq=input("there is a village nearby,will you want to 'wait' for boat or either 'swim'? ")
    if aq=="swim":
        print("you have been attacked by trouts")
    elif aq=="wait":
        door=input("Which door would you like to choose  red , blue or yellow ?" )
        if door=="red"and"blue":
            print("you have selected the wrong door")
        elif door=="yellow":
            print("excellent, you have found the ultimate treasure of asia worth billions.")
        else:
            print("please check the inputs.")
    else:
        print("Please check your inputs.")





elif direction=="right"or"Right":
    bq=input("There are three rooms :- 1,2,3 , In which room you would like to go ?")
    if bq=="1":
        print("you had been attacked by lion. you lose :( ")
    elif bq=="2":
        print("you lose because you are in fire room , bad choice :(")
    elif bq=="3":
        print("excellent, you have found the ultimate treasure of asia worth billions.")
    else:
        print("you have selected a wrong input")





else :
    print("The inputs are wrong ")
