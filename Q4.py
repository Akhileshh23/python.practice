''' Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique. '''

dic = {
    "kamal" : "html", 
    "akhi"  : "c",
    "chandu":"java",
    "jadu" : "python"
}

n = input("Enter name: ")
print(dic[n])