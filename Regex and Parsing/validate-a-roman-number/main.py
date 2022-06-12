# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

input_number = input()
numbers = []
for i in range(0,int(input_number)):
    valid = False
    phone_number = input()
    if str(phone_number)[0] in ["7", "8", "9"] and len(str(phone_number)) == 10 and phone_number.isdigit():
        valid = True
    if valid:
        print("YES")
    else:
        print("NO")
