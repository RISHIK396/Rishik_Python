import random
r_number=random.randrange(50)
print(r_number)
r_number=random.randrange(100,200)
print(r_number)
print(random.randint(0,5))

mychoice=random.choice(['1-swimming','2-badminton','3-cricket','4-basketball','5-hockey'])
print('my choice is:',mychoice)


colour=['cyan','blue','orange','red','green']
random.shuffle(colour)
print("reshuffled colour",colour)
random.shuffle(colour)
print("reshuffled colour",colour)
