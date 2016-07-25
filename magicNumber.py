import random

magic_number = [random.randint(0,9) , random.randint(0,9)]

def ask_user_check_number():
    user_number = int(input("Please insert an integer between 0 - 9 : "))
    if user_number in magic_number:
        return "Yay! You have found the magic number."

    else:
        return "Sorry! Plz try again."
    

def ask_user_for_attempt(attempt):
    for chances in range(attempt):
        print("This is your {} attempt".format(chances))
        print(ask_user_check_number())

user_attempt = int(input("How many attempt you want to try ? "))
ask_user_for_attempt(user_attempt)



