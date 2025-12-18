'''Write a program to create a dictionary of Hindi words with values as their English 
translation. Provide user with an option to look it up! '''

words = {
    "pani": "water",
    "ghar": "house",
    "kitab": "book",
    "ladka": "boy"
}

w = input("Enter Hindi word: ")
print(words[w])
