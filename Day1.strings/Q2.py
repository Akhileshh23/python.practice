'''Write a program to fill in a letter template given below with name and date.'''

Name = input("enter your name: ")
Date = int(input("enter yoy age: "))

letter = (f'''  
Dear <|{Name}|>, 
You are selected! 
<|{Date}|> 
''' )
print(letter)