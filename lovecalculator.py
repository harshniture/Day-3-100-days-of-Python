
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

whole_str = name1 + " " + name2
name = whole_str.lower()
love = name.count("l") + name.count("o") + name.count("v") + name.count("e")
true = name.count("t") + name.count("r") + name.count("u") + name.count("e")


score = str(true) + str(love)
a = int(score)

if a < 10 or a > 90:
    print("Your score is " + score + ", you go together like coke and mentos.")
elif a >= 40 and a < 50:
    print("Your score is " + score + ", you are alright together.")
else:
    print("Your score is " + score + ".")


