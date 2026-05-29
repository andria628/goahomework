point = 71
if point >= 90:
    print("A")
elif point >= 80 and point <= 90:    
    print("B")
elif point >= 70 and point <= 80:
    print("C")
elif point >= 60 and point <= 70:
    print("D")
else:
    print("F")

number = int(input("enter number: "))
if number >= 0:
    print("დადებითი")
else:
    print("უარყოფითი")

int1 = 15
int2 = 30
if int1 > int2:
    print("first number is better thansecond one")
elif int1 < int2:
    print("second number is better than first one")

num1 = int(input("enter your number: "))
if num1 % 2 == 0:
    print("odd")
else:
    print("even")