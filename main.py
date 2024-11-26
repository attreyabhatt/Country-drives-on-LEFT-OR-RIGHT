import random

# rhs - Right-hand side countries
# lhs - Left-hand side countries

rhs_file = open("rhs.txt")
rhs_countries = rhs_file.readlines() #readlines stores each line in a list
rhs_file.close()

lhs_file = open("lhs.txt")
lhs_countries = lhs_file.readlines() 
lhs_file.close()

print("\n" + "Welcome to right-left hand side drive country guesser")
print("Enter 'l' for LEFT and 'r' for RIGHT" + "\n")

while True:
    # since lhs countries are 1/3 of rhs countries to have a 50% chance of both type to appear we will use random
    random_number = random.randrange(0,3)

    if random_number == 2:
        random_rhs_country = random.choice(rhs_countries)
        random_rhs_country = random_rhs_country.strip()
        user_input = input(random_rhs_country + " drives on left or right?" + "\n")
    else:
        random_lhs_country = random.choice(lhs_countries)
        random_lhs_country = random_lhs_country.strip()
        user_input = input(random_lhs_country + " drives on left or right?" + "\n")

    if user_input == 'r':
        if random_number == 2:
            print("Correct" + "\n")
        else:
            print("Wrong" + "\n")

    if user_input == 'l':
        if random_number == 1 or random_number == 0:
            print("Correct" + "\n")
        else:
            print("Wrong" + "\n")





