'''Write a program to find out whether a given post is talking about “Harry” or not.'''

post = input("Enter post: ")

if("harry" in post.lower()):
    print("given post is talking about Harry")
else:
    print("given post is not talking about Harry")