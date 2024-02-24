#### ex1
import math
n=int(input("Input degree: "))
radian=math.radians(n)
print("Output radian: ",radian )

###### ex2
def trapezoid(base1,base2,height):
    return 0.5*(base1+base2)*height

height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))
print("EXpected output: ", trapezoid(base1,base2,height))

######## ex 3
import math

def regular_polygon(sides,length):
    return int((sides*(length**2))/(4*math.tan(math.pi/sides)))
sides=int(input("INput number of sides: "))
length=int(input("In[ut the length of a side: "))
print("The area of the polygon is: ", regular_polygon(sides,length))

###### ex 4
def parallelogram(length,height):
    return float(length*height)
length=int(input("Length of base: "))
height=int(input("Height of parallelogram: "))
print("Expected Ouput: ", parallelogram(length,height))