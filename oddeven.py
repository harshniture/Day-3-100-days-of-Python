#task 1 odd even

number = int(input("Which number you want to check?"))

if number == 0:
    print("0 is neither even nor odd number")
elif number % 2 == 0:
    print("This number is an even number")
else:
    print("This number is an odd number")