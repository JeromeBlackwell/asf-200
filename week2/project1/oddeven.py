
x1 =input("Enter a number to find out if its odd or even: ")
x1=int(x1)
if x1 %2 == 0:
    print(x1,( "is even number."))

else:
    print(x1,( "is odd number."))
    
#Extra credit

if x1 %4==0:
    print (x1,(" is a multiple of 4."))

num=input("Enter the number you want to divide: ")
num=int(num)
check=input("Enter a number you want to divide by: ")
check=int(check)

if num %check==0:
    print(num,("divides wonderfully with NO remainder"))

else:
    print("Remainder of "+str(num %check))


