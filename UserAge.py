
def print_age_seconds():
    age = int(input("Please enter your age in years : "))
    print("You have live for {} seconds for your age {}.".format(int(age*365*24*60*60), age))

print_age_seconds()
