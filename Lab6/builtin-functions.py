#### ex1
t=[1,2,3,4]
d1=eval("*".join(map(str,t)))
print(d1)

#### ex2
def countre(str):
    upp=sum(1 for char in str if char.isupper())
    low=sum(1 for char in str if char.islower())
    return upp , low
str="HelLo WorLd" 
print(countre(str))

##### ex 3
def is_pal_or_not(str):
    str=str.lower()
    rev=reversed(str)
    pal=''.join(rev)
    if pal==str:
        return True
    else: return False
p="Madam"
print(is_pal_or_not(p))

#### ex4
num=int(input())
miliseconds=int(input())
s=pow(num,0.5)
print(f"Square root of {num} after {miliseconds} miliseconds is {s}")

##### ex 5
tpl=(1,2,3,"h",True)
print(all(tpl))
tpl2=(2,0,"")
print(all(tpl2))