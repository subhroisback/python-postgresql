# Ask player for numbers
# Calculate lottery numbers
# Print out the winnings

import random

class sset(set):
    def __str__(self):
        return ', '.join([str(i) for i in self])

def get_user_input_numbers():
    user_input_csv = input("Please input 6 numbers between 1 - 20, separated by comma :")
    user_input_list = user_input_csv.split(",")
    user_input_set = {int(number) for number in user_input_list}
    return user_input_set



def get_lottery_generate_number():
    values = set()
    while len(values)<6:
        values.add(random.randint(0, 20))
    return values

def lottery_app_run():
    user_numbers = get_user_input_numbers()
    lottery_numbers = get_lottery_generate_number()
    number_matched = user_numbers.intersection(lottery_numbers)
    sset{} = number_matched
    print("Numbers matched {}. Your winnings are Rs.{}".format(number_matched, 100**len(number_matched)))

lottery_app_run()