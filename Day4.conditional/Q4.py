'''A spam comment is defined as a text containing following keywords: 
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams. '''

commet = input("Enter your commet: ")

if("Make a lot of money" in commet.lower() or
   "buy now" in commet.lower() or
   "subscribe this" in commet.lower() or
   "click this" in commet.lower()):
    print("This commet in spam")
    
else:
    print("The commet is not spam")