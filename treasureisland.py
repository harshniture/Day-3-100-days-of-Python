print("WELCOME TO TREASURE ISLAND !!")

a = (input("You are at a crossroad. Do you want to go left or right?"))
if a == "left":
    print(" Walking towards treasure.")
    b= input(" Ahh ! You came across a river. Do you want to swim or wait for the boat ?")
    if b == "wait" :
        print(" Hurray you have found the castle !")
        c = input(" Castle have three doors. Red door, blue door and yellow door. Which door do you want to enter ?")
        if c == "red door":
            print("Game Over ! You have lost the game.")
        if c == "blue door":
            print("Game Over ! You have lost the game.")
        if c == "yellow door":
            print("Hurray you have found the treasure !")
    else:
        print(" Crocodile ate you. Game Over !")
else:
    print(" You fell into hole. Game Over !")