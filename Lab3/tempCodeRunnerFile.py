###########    ex14
def reversed(str):
    p=str.split()
    words=p[::-1]
    words=" ".join(words)
    return words
a=input()
print(reversed(a))  