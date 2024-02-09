############    ex1
class Solution():
    def __init__(self):
        self.user_input = ""

    def getstring(self):
        self.user_input = input()

    def printString(self):
        print(self.user_input.upper())

s1 = Solution()
s1.getstring()
s1.printString()



############    ex2
class Shape():
     def area(self):
        return 0
     
class Square(Shape):
        def __init__(self,length):
            self.length = length
        def area(self):
             return self.length **2
        
a=int(input())
s1=Shape()
print(s1.area())
s2=Square(a)
print(s2.area())



############    ex3
class Shape():
     def area(self):
        return 0
     
class Rectangle(Shape):
    def __init__(self,length,width):
        self.width = width
        self.length=length
    def __str__(self):
        return f"{self.length},{self.width}"
    def area(self):
        return self.length*self.width

a=int(input())
b=int(input())
s1=Shape()
print(s1.area())
s2=Rectangle(a,b)
print(s2.area())



############    ex4
class Point:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def show(self):
        print("Coordinates: ({},{})".format(self.l,self.w))
    def move(self,x,y):
        self.l+=x
        self.w+=y
    def dist(self):
        return abs(self.l-self.w)
    
a=int(input())
b=int(input())
s1=Point(a,b)
s1.show()
move_x=int(input())
move_y=int(input())
s1.move(move_x,move_y)
s1.show()
print("Distance:",s1.dist())




############    ex5

class BankAccount:
    def __init__(self,name, balance):
        self.balance1 = balance
        self.name = name

    def owner(self):
        print("Owner's name:", self.name)

    def balance(self):
        print("Balance:", self.balance1)

    def deposit(self):
        while True:
            answer=input("Would you like to deposit? (y/n):".lower())
            if answer=="y":
                deposit1=int(input("Enter the desired deposit: "))
                if deposit1>=0:
                    self.balance1+=deposit1
                    print("Your {} is accepted: Current balance is: {}".format(deposit1, self.balance1))
                else:   
                    print("Error,your deposit should be lower than your balance")
            elif answer=="n":
                print("Deposite is not confirmed. ")
                break
            else:
                print("Error,Please nter y/n ")

    def withdraw(self):
        while True:
            answer1=input("Would you like to withdraw? (y/n):".lower())
            if answer1=="y":
                withdraw1=int(input("Enter the desired withdraw: "))
                if withdraw1>=0 and withdraw1<=self.balance1:
                    self.balance1-=withdraw1
                    print("Withdrawan:", withdraw1,"Current balance is: ", self.balance1)
                elif withdraw1>self.balance1:
                    print("Error")
                    break
                else:
                    print("Withdraw exceeds the current balance")
            elif answer1=="n":
                print("Deposite is not confirmed. ")
                break
            else:
                print("Eккor,Please enter y/n")

user_name=input("Name: ")
user_balance=int(input("Balance: "))

u1=BankAccount(user_name,user_balance)
u1.owner()
u1.balance()
u1.deposit()
u1.withdraw()


