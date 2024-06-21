#Q1 Quadratic EQ
"""a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
if a==0 :
	print("Wrong Quadratic Equation")

d = (b**2) - (4*a*c)  
if d==0:
	s1 = (-b-(d)**0.5)/(2*a) 
	print("Real And Equal Roots")
	print(s1)
	

else:
 s1 = (-b-(d)**0.5)/(2*a)  
 s2 = (-b+(d)**0.5)/(2*a)  
 print("Real And Unequal Roots")
 print(s1,s2)"""
 
 
 
#Question 3 part (i) print a pyramid
'''rows = int(input("Enter number of rows: "))


for i in range(rows):
    s=' '*(rows-i)
    st='*'*(2*i-1)
    print(s+st)
    '''
    
#Question 3 part (ii) Print a Reversed Pyramid
'''rows = int(input("Enter number of rows: "))

for i in range(rows-1,0,-1):
    st='*'*(2*i-1)
    s=' '*(rows-i)
    
    print(s+st)'''
    
#Question To check primr numbers    
"""def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_primes_till_num(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def get_first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

n = int(input("Enter a number: "))
if is_prime(n):
    print(n,"is a prime number")
else:
    print(n," is not a prime number")

print("All prime numbers till the entered number:")
print(get_primes_till_num(n))


print('First',n,"prime numbers:")
print(get_first_n_primes(n))"""


#Question 5 To find frequency , Replace,Remove all First And All Occurence

# Function to find the frequency of a character in a string
"""def char_frequency(str, char):
    count = 0
    for c in str:
        if c == char:
            count += 1
    return count

# Function to replace a character by another character in string
def replace_char(str, old_char, new_char):
    new_str = ""
    for c in str:
        if c == old_char:
            new_str += new_char
        else:
            new_str += c
    return new_str

# Function to remove the first occurrence of a character from a string
def remove_first_occurrence(str, char):
    new_str = ""
    found = False
    for c in str:
        if c == char and not found:
            found = True
            continue
        new_str += c
    return new_str

# Function to remove all occurrences of a character from a string
def remove_all_occurrences(str, char):
    new_str = ""
    for c in str:
        if c != char:
            new_str += c
    return new_str"""
    
#Question 6  to swap the first n characters of two strings
"""def swap_first_n_chars(s1, s2, n):
    s1_start = s1[:n]
    s2_start = s2[:n]
    s1 = s2_start + s1[n:]
    string2 = s1_start + s2[n:]
    return (s1, s2)"""
    
    
    
 #Question 8 Cube Of Even Numbers Of List
"""def gt_even_list(L):
  a=[]
  for i in L:
   if i%2==0:
        x=i**3
        a.append(x)
   else: 
          continue 
  print(a)"""
  
  
  
#Question 10 Define Class Point And Find Distance Between Coordinates
"""class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def distance(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5
       """
#Question 11 Function To Get a Dictionary With Keys 1-5 and Values as Cubes Of Keys

"""def print_dict_cubes():
    d = {}
    for i in range(1, 6):
        d[i] = i**3
    print(d)"""
  
#Ouestion 4 Accept a Character Check  its Case and If Number Write its Alphabetical Name'

"""x=input("your Character:")
if x.isalpha() and x.isupper():
  print("UpperCase")
if x.isalpha() and x.islower():
  print("lowerCase")
if x.isdigit():
    if x=='0':
        print("Zero")
    if x=="1'':
        print("One")
    if x=='2':
        print("Two")
    if x=='3':
        print("Three")
    if x=='4':
        print("Four")
    if x=='6':
        print("One")
    if x=='7':
        print("Seven")
    if x=='8':
        print("Eight")
    if x=='9':
        print("Nine")"""
        
#Question 12 Take a Tuple Peform Functions On it        
"""t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
r=[]
half = len(t1)//2
print(t1[:half])
print(t1[half:])
    
for i in t1:
	if i%2==0:
		r.append(i)
print("Even Tuple",tuple(r))

t2 = (11, 13, 15)
print(t1 + t2)
		
		
print("Max-",max(t1))
print("Min-",min(t1))

"""
#Question 7 Accept String And Sub String And Tell Indices of Sub String
"""def f_occ(sttr,sub):
  ind=0
  r=[]
  for i in sttr:
    ind=ind+1
    if i==sub:
        r.append((ind-1))
  	  
  if r==[]:
      print(-1)
  else:
      print(r)"""
'''#Question 13 Error
def yr_name():
    n = input("Enter your name: ")
    for c in n:
        if not c.isalpha():
            raise ValueError("Name can only contain letters")
    return n

try:
    print("Your name is:", yr_name())
except ValueError as error:
    print("Error:", error)'''
