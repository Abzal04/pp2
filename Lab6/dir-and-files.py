# # ###### ex1
import os
for dirpach, dirnames, filenames in os.walk('•'):
      for dirname in dirnames:
            print('only dir and files: ', os.path.join(dirpach, dirname))
      for filename in filenames:
            print('all:', os.path.join (dirpach,filename))
# # ####### ex2
import os 

def test_access(path):
      a=os.path.exists(path),
      b=os.access(path,os.R_OK)
      c=os.access(path,os.W_OK)
      d=os.access(path,os.X_OK)
      return a,b,c,d
path="Lab1/comments.py"
print(test_access(path))

# ##### ex3
import os
path="Lab1"
print(os.path.exists(path))
print(os.listdir(path))

###### ex4
import os
with open("123.txt","r") as f:
    counter=0
    for line in f:
      counter+=1
    print(counter)

##### ex5
import  os
with open("123.txt","a") as f:
     f.write()
     f.close()

##### ex6
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

###### ex8
import os
a=os.path.exists("LL/r.txt")
s=os.access(path,os.W_OK)
b=os.remove("LL/r.txt")
       