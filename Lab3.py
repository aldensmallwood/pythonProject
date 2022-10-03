# Lab 3, population
# Alden Smallwood

years = int(input("Please enter number of years: "))

y = years
pop = 89.2


def function_m(p):  # this function takes a parameter and returns the same value multiplied by 1.023
    return p * 1.023


def function_d(p):  # this function takes a parameter and returns the same value divided by 1.023
    return p / 1.023


while y != 0:  # while y does not equal zero, multiply or divide the population by 1.023 and make y one closer to 0
    # this will provide for the correct number of iterations to accurately calculate the population and imitates
    # exponentiation
    if y > 0:
        pop = function_m(pop)
        y -= 1
    else:
        pop = function_d(pop)
        y += 1

print("The population of Mexico in ", 1990 + years, " is ", pop, " million")

popInput = int(input("Enter the population: "))
year = 0
pop1 = 89.2

if 89.2 < popInput:  # if the input population is greater than 89.2, multiply the pop1 by 1.023 and increment year
    # until mexico's population (pop1) exceeds the input one --> this will return the years that it takes to reach input
    while popInput > pop1:
        pop1 = function_m(pop1)
        year += 1

else:  # the input population is less than 89.2 --> while mexico's population is greater than the popInput, divide
    # mexico's population by 1.023 and decrement year, that way it calculates how many years are needed until the
    # population of mexico reaches the input
    while pop1 > popInput:
        pop1 = function_d(pop1)
        year -= 1


print("Pop in year: ", 1990 + year, " is equal to ", pop1)
