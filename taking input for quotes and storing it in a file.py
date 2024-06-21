def create_quotes():
    f=open("quote.txt",'w+')
    while True:
        str=input("enter the quote")
        str='\n'
        f.write(str)
        print("want to enter more quotes: ")
        ans=input()
        if ans.lower()=='no':
            break
    f.close()
create_quotes()
