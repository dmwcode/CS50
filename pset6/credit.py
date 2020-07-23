from cs50 import get_int
from cs50 import get_string

s = get_string("Number:  ")
while s.isdigit() is False:
    s = get_string("Number:  ")

even = []
odd = []
even_x_two = []
odd_x_two = []

if len(s) % 2 == 0:
    #print("String has even number of items:  ")
    for i in range(0, len(s), 2):
        int(s[i])
        # Add to list, starting at 0, every other item
        even.append(int(s[i]))
        # Multiple by 2 and add to 2nd list
        even_x_two.append(int(s[i]) * 2)
    for i in range(1, len(s), 2):
        int(s[i])
        odd.append(int(s[i]))
        odd_x_two.append(int(s[i]) * 2)
    odd_sum = sum(map(int, odd))
    # Sums the list, splits any string integers over 10 into 2 digits ex. 1,2
    even_x_two_sum = sum(list(map(int,"".join(map(str, even_x_two)))))
    #Generate checksum (Luhn's Alg.)
    checksum_even = even_x_two_sum + odd_sum
    if checksum_even % 10 != 0:
        print("INVALID\n")
    elif len(s) == 16 and s[0:1] is '4':
        print("VISA\n")
    elif len(s) == 16 and s[0:2] is '51' or '52' or '53' or '54' or '55':
        print("MASTERCARD\n")
elif len(s) % 2 != 0:
    for i in range(1, len(s), 2):
        int(s[i])
        odd.append(int(s[i]))
        odd_x_two.append(int(s[i]) * 2)
    for i in range(0, len(s), 2):
        int(s[i])
        even.append(int(s[i]))
        even_x_two.append(int(s[i]) * 2)
    even_sum =  sum(map(int, even))
    odd_x_two_sum = sum(list(map(int,"".join(map(str, odd_x_two)))))
    checksum_odd = odd_x_two_sum + even_sum
    if checksum_odd % 10 != 0:
        print("INVALID\n")
    elif len(s) == 13 and s[0:1] is '4':
            print("VISA\n")
    elif len(s) == 15 and s[0:2] is '34' or '37':
            print("AMEX\n")
    

# Use map to pass sum method to list of string numbers?
# even_x_two_sum = sum(map(int, even_x_two))
# odd_x_two_sum = sum(map(int, odd_x_two))
# even_sum =  sum(map(int, even))
# odd_sum = sum(map(int, odd))

###  Print list with loop
#for x in range(len(even_x_two)):
#    print(f"Printing list even_x_two {even_x_two[x]}")

#print(*even, sep='')
#print(*odd, sep='')
