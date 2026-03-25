num=int(input("enter a number to check:"))
if num>50:
    print("number is greater than 50",end=" ")
    if num%2==0:
        print("and it is even too")
    else:
        print("it is an odd number")

else:
    print("the number is less than 50")
