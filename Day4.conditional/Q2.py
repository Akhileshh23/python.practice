''' Write a program to find the greatest of four numbers entered by the user.'''

a = int(input("Enter no: "))
b = int(input("Enter no: "))
c = int(input("Enter no: "))
d = int(input("Enter no: "))

if(a>b and a>c and a>d):
    print("Greater number is: ",a)
elif(b>a and b>c and b>d):
    print("Greater number is: ",b)
elif(c>b and c>a and c>d):
    print("Greater number is: ",c)
elif(d>b and d>c and d>a):
    print("Greater number is: ",d)