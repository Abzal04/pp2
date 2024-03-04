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
with open("123.txt","a") as f:
     f.write(list[1,23,4])
     f.close()