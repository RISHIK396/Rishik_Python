#objective-to calculate number of vowels,digits and special characters in a string entered by the user
#input- str1:input
#output-printing the number of vowels,digits,special charaters in a string
str1=input("enter any sentence:")
c_alpha=0
c_uppercase=0
c_lowercase=0
c_vowel=0
c_consonant=0
c_spec=0
c_digit=0

for i in str1:
    if i.isalpha():
        c_alpha+=1
        if i.lower()in 'aeiou':
            c_vowel+=1
        elif i.isupper():
            c_uppercase+=1
        elif i.islower():
            c_lowercase+=1
        elif i.lower()in 'bcdfjklmnpqrstvwxyz':
            c_consonant+=1
    elif i.isdigit():
        c_digit+=1
        if i==0:
            print("THE NUMBER IS ZERO")
        elif i==1:
            print("THE NUMBER IS ONE")
        elif i==2:
            print("THE NUMBER IS TWO")
        elif i==3:
            print("THE NUMBER IS THREE")
        elif i==4:
            print("THE NUMBER IS FOUR")
        elif i==5:
            print("THE NUMBER IS FIVE")
        elif i==6:
            print("THE NU8MBER IS SIX")
        elif i==7:
            print("THE NUMBER IS SEVEN")
        elif i==8:
            print("THE NUMBER IS EIGHT ")
        elif i==9:
            print("THE NUMBER IS NINE")
    else:
        c_spec+=1
print("THE NUMBER OF ALPHABETS IN THE STRING ARE:",c_alpha)
print("THE NUMBER OF VOWELS ARE:",c_vowel)
print("THE NUMBER OF ALPHABETS IN LOWER CASE ARE:",c_lowercase)
print("THE NUMBER OF ALPHABETS IN UPPER CASE ARE:",c_uppercase)
print("THE NUMBER OF CONSONANTS IN THE STRING ARE:",c_consonant)
print("THE NUMBER OF DIGITS IN THE STRING ARE:",c_digit)
print("THE NUMBER OF SPECIAL CHARACTERS IN THE STRING ARE:",c_spec)
