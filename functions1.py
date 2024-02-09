###########    ex1
def funct(ounces):
    gram =ounces*28.3495231
    print(gram)

a=float(input())
result=funct(a)

###########    ex2
def centigrade(fahrenheit):
    C = (5 / 9) * (fahrenheit-32)
    print(C)

a=float(input())
result=centigrade(a)

############    ex3
def solve(numheads,numlegs):
    # (35-x)*2+x*4=94
    x=(4*numheads-numlegs)/2
    y=numheads-x
    return int(x),int(y)

a=int(input())
b=int(input())
print(solve(a,b))

###########    ex4
def filter_prime(prime):
    if prime<=1:
        return False
    elif prime<=3:
        return True
    elif prime%2 == 0 or prime%3 == 0:
        return False
    

###########    ex5
from itertools import permutations
def permutations1(a):
    p = permutations(a)
    for i in p:
        print("".join(i))
str=input()
permutations1(str)
        
###########    ex6
def reversed(str):
    p=str.split()
    words=p[::-1]
    words=" ".join(words)
    return words
a=input()
print(reversed(a))

###########    ex7
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
print(has_33([1, 3, 3]))   
print(has_33([1, 3, 1, 3]))    
print(has_33([3, 1, 3])) 

###########    ex9
import math
def volume(sphere):
    volume=(4/3)* math.pi * pow(sphere,3)
    return volume
radius=float(input())
print(volume(radius))
        

###########    ex10
def unique_elements(list):
    unique_list= []
    for el in list:
        if el not in unique_list:
            unique_list.append(el)
    return unique_list
list = [1, 2, 2, 3, 3, 4, 5, 5]
print(list)
print(unique_elements(list))

###########    ex11
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]
word = input()
if is_palindrome(word):
    print("is palindrome.")
else:
    print("is not palindrome.")

###########    ex12
def histogram(nums):
    for num in nums:
        print("*"*num)

histogram([4,9,7])

############ ex13
import random
def program():  
    print('Hello! What is your name?')
    name=input()
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    secret_num=random.randint(1,20)
    attempts=0
    while True:
        print("Take a guess.")
        guess =int(input())
        attempts+=1
        if guess<secret_num:
            print("Your guess is too low.")
        elif guess> secret_num:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

program()


