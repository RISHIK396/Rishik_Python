#dictionary is nothing but key value pairs
#create a dictionary and take input from the user and return the meanining of word the dictionary
word=input("enter the word whose meaning you want to get:")
dict1={"mutable":"it means we can modify or make changes","immutable":"it means cannot make changes","procrastination":"delaying things","sets":"a well defined collection of objects"}
meaning=dict1[word]
print(meaning)
