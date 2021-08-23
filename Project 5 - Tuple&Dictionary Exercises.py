            ###### TUPLE EXERCISES #####

'''Problem-1: A number is a magic number if the summation of even indexed
digits is equal to the summation of odd indexed digits. Now, write
 a Python program that will take a number N in the very first line
from the user, then take N number of test cases in the next N lines.
The program should print a tuple containing two sub-tuples , where
the first sub-tuple will hold the magic numbers and the second sub-tuple
will hold the non-magic numbers'''
#*** SOLVE ***
n = int(input("Enter N:"))
list1 = []
magic = []
not_magic = []
for i in range(n):
    numb = input("Enter A Number:")
    list1.append(numb)
###print(list1)
for numbers in list1:
    odd = 0
    even = 0
    for f in range(len(numbers)):
        if f%2 == 0 :
            even +=int(numbers[f])
        else:
            odd +=int(numbers[f])
    if even == odd:
        magic.append(int(numbers))
    else:
        not_magic.append(int(numbers))
final = []
final.append(tuple(magic))
final.append(tuple(not_magic))
final = tuple(final)
print(final)

'''Problem-2: Write a Python program that takes a tuple of tuples.
Calculate the average value of the numbers for each tuple
of tuples and find the tuple whose sum is the maximum.
[Try to avoid built in functions]'''
#*** SOLVE ***
### Taking tuples in a tuples as input :
n = int(input("How many tuples do you want:"))
main_list = []
for i in range(n):
    user_input =list(map(int,input("Enter tuple values using coma(,):").split(",")))
    main_list.append(tuple(user_input))
main_tuple = tuple(main_list)
### Sorting out the average and Tuple with maximum sum:
avg_list = []
max = 0
max_tuple = []
for tuples in main_tuple:
    total = 0
    for items_2 in tuples:
        total += items_2
    avg = total/len(tuples)
    avg_list.append(avg)
    if total > max:
        max = total
        max_tuple = tuples
print("Average :",avg_list)
print("Tuple with maximum sum :",max_tuple)


'''Problem-3: We all know that the additive primaries are red, green, and blue.
Now, write a Python program that will take a color sequence as a string from the user
where R represents Red , G represents Green and B represents Blue .The program
should print the choice of colors that is actually a tuple containing the sub-tuples as
(color_name, color_frequency) iff the color_frequency for that color is at least one in the
given color sequence.'''
#*** SOLVE ***
user_input = input("Enter Additive primary colors (R,G,B):")
total_red = 0
total_green = 0
total_blue = 0
for letter in user_input:
    if letter == "R":
        total_red += 1
    elif letter == "G":
        total_green += 1
    elif letter == "B":
        total_blue+= 1
list_red = ["Red"]
list_red.append(total_red)
tuple_red = tuple(list_red)
list_green = ["Green"]
list_green.append(total_green)
tuple_green = tuple(list_green)
list_blue = ["Blue"]
list_blue.append(total_blue)
tuple_blue = tuple(list_blue)

tuple_final = tuple([tuple_red,tuple_green,tuple_blue])
print(tuple_final)

            ###### DICTIONARY EXERCISES #####

'''Problem-1: Suppose dictionaries are given .Write a Python program that combines two or more
dictionaries, creates a list of values for each key.'''
#*** SOLVE ***
dict1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
dict2 = {'x': 300, 'y': 'Red', 'z': 600}
dict3 = {}
for key1,item1 in dict1.items():
    flag = 0
    for key2,item2 in dict2.items():
        if key1 == key2:
            dict3[key1] = [item1,item2]
            break
        else:
            dict3[key1] = item1
print(dict3)

'''Problem-2: Suppose,there will be a dictionary named dict_1.The values of the dictionary will be a
list or a tuple.Here, in a key value pair ,the key will be a lower case letter if the value is a
list . And if the value is a tuple,then the key will be an uppercase letter.
Write a Python program that creates a new dictionary named “dict_primes” which
contains only prime numbers in the value.And print the dictionary dict_primes.'''
#*** SOLVE ***
dict_1 = {"N":(4,9,3),"k":[95,37,197],"F":(32,5,97),"s":[31,94,55]}
dict_primes = {}
empty_list = []
def prime_check(num) :
    flag = 0
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = 1
                break
    if flag == 0:
        return num

for key,value in dict_1.items():
    list_uni = []
    if ord(key) >= 65 and ord(key) <=90:
        for numbers in value:
            if prime_check(numbers) != None:
                list_uni.append(prime_check(numbers))
            else:
                list_uni.extend(empty_list)
            dict_primes[key] = tuple(list_uni)
    elif ord(key) >= 97 and ord(key) <=122:
        for numbers in value:
            if prime_check(numbers) != None:
                list_uni.append(prime_check(numbers))
            else:
                list_uni.extend(empty_list)
            dict_primes[key] = list_uni
print("dict_primes=",dict_primes)

'''Problem-3: An Agent has three normal skills along with an ultimate skill. Furthermore, there are
three agents in the game named after Rage , Jett and Sage .Now, write a Python
program that will detect the Agent from a given dictionary where the keys are "Normal
Skills", "Ultimate Skill" and the values are the damages due to the use of the skills on the
opponents.
Additive Damage Score: SUM_TOTAL(NORMAL_SKILL_DAMAGE,
ULTIMATE_SKILL_DAMAGE)

Constraints:
1. If the additive damage score is less than or equal to 70 then it is Rage .
2. Else If the additive damage score is less than or equal to 100 then it is Jett .
3. Else it is Sage .'''
#*** SOLVE ***
d = {"Normal Skills": [10, 15, 20], "Ultimate Skill": 50}
additive_damage = 0
for value in d.values():
    if type(value) == list:
        for key in value:
            additive_damage += int(key)
    elif type(value) == int:
        additive_damage += value

if additive_damage <= 70:
    print("Rage!")
elif additive_damage <= 100:
    print("Jett!")
else:
    print("Sage!")