##### ex1
def square(n):
    for i in range(n+1):
        yield i**2
n=int(input())
for num in square(n):
    print(num)


###### ex2 
def even_num(n):
    for i in range(n+1):
        if i%2==0:
            yield i
n=int(input())
print(", ".join(str(num) for num in even_num(n)))

###### ex 3
def divisible(n):
    for i in  range(n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
for num in divisible(n):
    print(num)

####ex 4
def squares(a,b):
    for i in range(a,b+1):
        yield i**2
a=int(input())
b=int(input())
print("\n")
for num in squares(a,b):
    print(num)


###### ex 5
def generator(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
print("\r")
for num in generator(n):
    print(num)