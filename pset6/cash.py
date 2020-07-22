from cs50 import get_float

counter = 0

n = get_float("Change owed?  ")
while n < 0:
    n = get_float("Change owed  ")
    break
#  Converting float to round number 
cents = round(n * 100)

for cent in range(int(cents)):
    while cents >= 25:
        cents = cents - 25
        counter += 1
    while cents >= 10:
        cents = cents - 10
        counter += 1
    while cents >= 5:
        cents = cents - 5
        counter += 1
    while cents >= 1:
        cents = cents - 1
        counter += 1
    
print(f"{counter}")
