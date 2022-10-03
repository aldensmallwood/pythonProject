# Lab 4, random array
# Alden Smallwood

# part 1
import array as arr
import random
ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(len(ran)):  # traversing the array ran and filling it with random ints from 1 to 20
    ran[x] = random.randint(1, 20)

print(ran)

total = 0.0
small = ran[0]

for x in range(len(ran)):  # traversing x, adding up all the elements and finding the smallest element by checking each
    # value and setting the variable small equal to that value if it is smaller than previous set value
    total += ran[x]
    if ran[x] < small:
        small = ran[x]


print("The mean is ", total / len(ran))
print("Your smallest number is ", small)

# part 2

num = int(input("Enter in a number: "))

list1 = []

ind = 0

while int(num / 10 != 0):  # while num / 10 does not equal 0, or while there are still digits to be added to the list,
    # insert num % 10 or the one's digit into the list at index 0 --> then divide num by 2 to get next digit
    list1.insert(0, num % 10)
    num = int(num / 10)


print("Your array is: ", list1)

# part 3

ran2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ran3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(len(ran2)):  # traversing the array ran2 and ran3 and filling them with random ints from 1 to 20
    ran2[x] = random.randint(1, 20)
    ran3[x] = random.randint(1, 20)

ranBoth = []

y = 0
for x in range(len(ran2 + ran3)):  # this adds the 10 elements of ran2 to the new array and sorts them (they are already
    # sorted), and then it adds the 10 elements of ran3 to the new array and sorts them as each one is added
    if x < 10:  # adding 10 elements of ran2 to ranBoth
        ranBoth.insert(x, ran2[x])
    else:  # adding 10 elements of ran3 to ranBoth
        ranBoth.insert(x, ran3[x - 10])
    ranBoth.sort()

print(ranBoth)


