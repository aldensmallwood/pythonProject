

# Lab 1, calculating a salary
# Alden Smallwood

salary = int(input("Enter your salary:"))
if salary < 1:
    print("Error, salary has to be positive")
else:
    hours = int(input("Enter your hours:"))
    if hours < 0:
        print("Error, hours has to be positive")
    else:
        if hours > 40:
            print("You earned ", 40 * salary + (hours - 40) * 1.5 * salary, " dollars")
        else:
            print("You earned ", hours * salary, " dollars")



