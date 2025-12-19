''' Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user. '''

e = int(input("Enter your marks: "))
m = int(input("Enter your marks: "))
s = int(input("Enter your marks: "))

total = (e+m+s)/3

if(e>=33 and m>=33 and s>=33 and total>=40):
    print("Your Are Passed")
else:
    print("Your Are Failed")