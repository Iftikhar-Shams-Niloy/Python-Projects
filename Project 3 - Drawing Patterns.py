#Drawing Rectangle:
print("<<<Drawing Rectangle>>>")
n1 = int(input("Enter number of rows :"))
n2 = int(input("Enter number of collumns:"))
for i1 in range(n1):
    for j1 in range(n2):
        print(j1+1,end=" ")
    print()

#Drawing Triangle-1:
print("___________________________")
print("<<<Drawing Triangle-1>>>")
n3 = int(input("Enter a Number:"))
num = 1
for i2 in range(n3):
    for j2 in range(num):
        print("*",end=" ")
    print()
    num += 1

#Drawing Triangle-2:
print("___________________________")
print("<<<Drawing Triangle-2>>>")
n3 = int(input("Enter a Number:"))
num = 1
for i2 in range(n3):
    for j2 in range(num):
        print(j2+1,end=" ")
    print()
    num += 1

#Drawing Triangle-3:
print("___________________________")
print("<<<Drawing Triangle-3>>>")
n4 = int(input("Enter a Number:"))
num = 1
for i in range(n4):
    for j in range(n4-num):
        print(" ",end=" ")
    for k in range(num):
        print("*",end=" ")
    num += 1
    print()

#Drawing Triangle-4:
print("___________________________")
print("<<<Drawing Triangle-4>>>")
n4 = int(input("Enter a Number:"))
num = 1
for i in range(n4):
    num2 = 1
    for j in range(n4-num):
        print(" ",end=" ")
    for k in range(num):
        print(num2,end=" ")
        num2 += 1
    num += 1
    print()

#Drawing Triangle-5:
print("___________________________")
print("<<<Drawing Triangle-5>>>")
n5 = int(input("Ente a Number:"))
num = 1
num2 = 1
for i in range(n5):
    for j in range(n5-num):
        print(" ",end=" ")
    for k in range(num2):
        print("*",end=" ")
    print()
    num += 1
    num2 += 2

#Drawing Triangle-6:
print("___________________________")
print("<<<Drawing Triangle-6>>>")
n5 = int(input("Ente a Number:"))
num = 1
num2 = 1
for i in range(n5):
    for j in range(n5-num):
        print(" ",end=" ")
    for k in range(num2):
        print(k+1,end=" ")
    print()
    num += 1
    num2 +=2

#Drawing Rombus-1:
print("___________________________")
print("<<<Drawing Rombus-1>>>")
n5 = int(input("Enter a Number :"))
num = 1
num2 = 1
for i in range(n5):
    for j in range(n5-num):
        print(" ",end=" ")
    for k in range(num2):
        print("*",end=" ")
    print()
    num += 1
    num2 += 2
num = 1
num2 = 3
for i in range(n5-1):
    for j in range(num):
        print(" ",end=" ")
    for k in range(n5*2-num2):
        print("*",end=" ")
    print()
    num += 1
    num2 += 2

#Drawing Rombus-2:
print("___________________________")
print("<<<Drawing Rombus-2>>>")
n5 = int(input("Enter a Number :"))
num = 1
num2 = 1
for i in range(n5):
    for j in range(n5-num):
        print(" ",end=" ")
    for k in range(num2):
        print(k+1,end=" ")
    print()
    num += 1
    num2 += 2
num = 1
num2 = 3
for i in range(n5-1):
    for j in range(num):
        print(" ",end=" ")
    for k in range(n5*2-num2):
        print(k+1,end=" ")
    print()
    num += 1
    num2 += 2

#Drawing Hollow Rectangle-1:
print("___________________________")
print("<<<Drawing Hollow Rectangle-1>>>")
print("<<<Drawing Rectangle>>>")
n1 = int(input("Enter number of rows :"))
n2 = int(input("Enter number of collumns:"))
for i1 in range(n1):
    for j1 in range(n2):
        if i1 == 0 or i1 == (n1-1) or j1 == 0 or j1 == (n2-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#Drawing Hollow Rectangle-2:
print("___________________________")
print("<<<Drawing Hollow Rectangle-2>>>")
n1 = int(input("Enter number of rows :"))
n2 = int(input("Enter number of collumns:"))
for i1 in range(n1):
    for j1 in range(n2):
        if i1 == 0 or i1 == (n1-1) or j1 == 0 or j1 == (n2-1):
            print(j1+1,end=" ")
        else:
            print(" ",end=" ")
    print()

#Drawing Hollow Triangle-1:
print("___________________________")
print("<<<Drawing Hollow Triangle-1>>>")
n3 = int(input("Enter a Number:"))
num = 1
for i2 in range(n3):
    for j2 in range(num):
        if i2 ==0 or i2 == (n3-1) or j2 == 0 or j2 ==(num-1) :
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()
    num += 1

#Drawing Hollow Triangle-2:
print("___________________________")
print("<<<Drawing Hollow Triangle-2>>>")
n3 = int(input("Enter a Number:"))
num = 1
for i2 in range(n3):
    for j2 in range(num):
        if i2 ==0 or i2 == (n3-1) or j2 == 0 or j2 ==(num-1) :
            print(j2+1,end=" ")
        else:
            print(" ", end=" ")
    print()
    num += 1

#Drawing Hollow Trianlge-3
print("___________________________")
print("<<<Drawing Hollow Triangle-3>>>")
n4 = int(input("Enter a Number:"))
num = 1
for i in range(n4):
    for j in range(n4-num):
        print(" ",end=" ")
    for k in range(num):
        if i ==0 or i == (n4-1) or k == 0 or k ==(num-1) :
            print("*",end=" ")
        else:
            print(" ", end=" ")
    num += 1
    print()

#Drawing Hollow Triangle-4
print("___________________________")
print("<<<Drawing Hollow Triangle-4>>>")
n4 = int(input("Enter a Number:"))
num = 1
for i in range(n4):
    for j in range(n4-num):
        print(" ",end=" ")
    for k in range(num):
        if i ==0 or i == (n4-1) or k == 0 or k ==(num-1) :
            print(k+1,end=" ")
        else:
            print(" ", end=" ")
    num += 1
    print()

#Drawing Hollow Triangle-5
print("___________________________")
print("<<<Drawing Hollow Triangle-5>>>")
n5 = int(input("Ente a Number:"))
num = 1
num2 = 1
for i in range(n5):
    for j in range(n5-num):
        print(" ",end=" ")
    for k in range(num2):
        if i == 0 or i==(n5-1) or k == 0 or k==(num2-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    num += 1
    num2 +=2

#Drawing Hollow Triangle-6
print("___________________________")
print("<<<Drawing Hollow Triangle-6>>>")
n5 = int(input("Ente a Number:"))
num = 1
num2 = 1
for i in range(n5):
    for j in range(n5-num):
        print(" ",end=" ")
    for k in range(num2):
        if i == 0 or i==(n5-1) or k == 0 or k==(num2-1):
            print(k+1,end=" ")
        else:
            print(" ",end=" ")
    print()
    num += 1
    num2 +=2

#Drawing Hollow Rombus-1
print("___________________________")
print("<<<Drawing Hollow Rombus-1>>>")
n5 = int(input("Enter a Number :"))
num = 1
num2 = 1
for i in range(n5):
    for j in range(n5-num):
        print(" ",end=" ")
    for k in range(num2):
        if i==0 or k==0 or k==num2-1:
            print(k+1,end=" ")
        else:
            print(" ",end=" ")
    print()
    num += 1
    num2 += 2
num = 1
num2 = 3
for i in range(n5-1):
    for j in range(num):
        print(" ",end=" ")
    for k in range(n5*2-num2):
        if  i ==n5-1 or k==0 or k==(n5*2-num2-1):
            print(k+1,end=" ")
        else:
            print(" ",end=" ")
    print()
    num += 1
    num2 += 2