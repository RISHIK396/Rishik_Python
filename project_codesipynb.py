# -*- coding: utf-8 -*-
"""project_codesipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JPVrKfTnUt9kNG2BiY9Ayocq0SqT5S7_
"""

#Adding as many number as you want 
def adding_numbers():
  num=0
  while True:
    choice=input("do you want to enter numbers: ")
    if choice.lower()=='yes':
      num1=int(input("enter the number which is to be added: "))
      num2=int(input("enter the number 2 which is to be added: "))
      num+=num1+num2
    else:
      break
  return num
x=adding_numbers()
print(x)

#performing division till a user want to do
def dividing_numbers():
  list1=[]
  while True:
    choice=input(" do you want to do division choice: ")
    if choice.lower()=='yes':
      num1=int(input("enter the first number: "))
      num2=int(input("enter the second number: "))
      num=num1/num2
      list1.append(num)
    else:
      break
  for i in list1:
    print("the",list1.index(i)+1,"division came to be: ",i)
dividing_numbers()

#peforming floor division till the user want to do
def floor_division():
  list1=[]
  while True:
    choice=input("enter your choice whether you want to perform floor division: ")
    if choice.lower()=='yes':
      num1=eval(input("enter the first number: "))
      num2=eval(input("enter the second number: "))
      num=num1//num2
      list1.append(num)
    else:
      break
  for i in list1:
    print("the",list1.index(i)+1,"floor division performed is: ",i)

floor_division()

#performing modulus function
def modulo_function():
  list1=[]
  while True:
    choice=input("enter your choice whether you want to perform modulous division: ")
    if choice.lower()=='yes':
      num1=eval(input("enter the first number: "))
      num2=eval(input("enter the second number: "))
      num=num1%num2
      list1.append(num)
    else:
      break
  for i in list1:
    print("the",list1.index(i)+1,"modulous performed is: ",i)
modulo_function()

#performing exponentiation function
def exponent():
    list1=[]
    while True:
      choice=input("do you want to perform exponentitation: ")
      if choice.lower()=='yes':
        num1=int(input("enter the number whose exponent is to be found: "))
        power=int(input("enter the number by which you want to do power:  "))
        num=num1**power
        list1.append(num)
      else:
        break
    for i in list1:
      print("the exponentiation of",list1.index(i)+1,"is ",i)
exponent()

def complex():
  num1=eval(input("enter the first complex number: "))
  num2=eval(input("enter the second complex number: "))
  while True:
    chr=input("enter the operation to be performed  * ,/,+,-: ")
    if chr=='+':
      print(num1+num2)
    elif chr=='-':
      print(num1-num2)
    elif chr=='*':
      print(num1*num2)
    elif chr=='/':
      print(num1/num2)
    else:
      print("please enter a valid input")
    choice=input("do you want to perform any other operation: ")
    if choice.lower()=='yes':
      pass
    else:
      break
complex()