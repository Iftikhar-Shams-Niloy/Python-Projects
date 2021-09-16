'''1.Write Python code of a program that reads a number as a year and determines whether it is a leap
year or not.'''
print("Solution of 1:")
user_input = int(input("Enter a year: "))
if (user_input%4) == 0:
   if (user_input%100) == 0:
       if (user_input%400) == 0:
           print(f"{user_input} is  LEAP YEAR.")
       else:
           print(f"{user_input} is NOT LEAP YEAR.")
   else:
       print(f"{user_input} is LEAP YEAR.")
else:
   print(f"{user_input} is NOT LEAP YEAR.")

'''2.Write a Python program that reads a number and finds the sum of the series of 1 +11 + 111 + 1111
+ ….+N terms.'''
print("_____________________________")
print("Solution of 2:")
n = int(input("Enter a number:"))
sub_total = 0
total = 0
for i in range(n):
    sub_total += (10**i)
    if i < (n-1):
        print(sub_total,end="+")
    else:
        print(sub_total)
    total += sub_total
print("The Sum is :",total)

'''3.Write a Python program that reads a number and displays the multiplication table of the given
integer.'''
print("_____________________________")
print("Solution of 3:")
n = int(input("Enter a number:"))
for i in range(10):
    print(f"{n} X {i+1} = {n*(i+1)}")

'''4.Write a python program that takes integer inputs from the user until the user gives "Stop".
Print average and product of all numbers.'''
print("_____________________________")
print("Solution of 4:")
flag = 0
total = 0
count = 0
while flag == 0:
    numbers = input("Enter A Number:")
    if numbers != "Stop":
        total += int(numbers)
        count += 1
    else:
        break
avg = total/count
print("Total :",total)
print("Average :",avg)

'''5.Write a python program that prints alphabet pattern 'Z' of size N using * where N will be given as
input.'''

n = int(input("Enter a number:"))
result=""
for i in range(n):
    for j in range(n):
        if (((i == 0 or i == (n-1)) and j >= 0 and j <= (n-1)) or i+j==(n-1)):
            result=result+"*"
        else:
            result+=" "
    result+="\n"
print(result)
