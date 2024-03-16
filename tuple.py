a=(1,2,3,4,5,5,6,6,7,8,9)
b=("jhon","hanish","wick")
c=(2.3,2.5,3.14,6.66)
d=(61)
e=(a,b)
f=[1,2,3,4,5,6,7,8]
h=(4,15,787,2,5,7,2,5,1)
print(a,type(a),len(a))#gives the length of the tuple and print the tuple
print(b,type(b))#prints the tuple b
print(c,type(c))#prints the tuple c
print(d,type(d))#prints the tuple d
print(a[0])#gives value according to the index
print(a[-2])#gives value according to the index
print(a[-2:])# slices the tuple and gives values according to the tuple updated
print(min(a))#gives minimum value of a
print(max(a))#gives maximum value of a
print(a.count(1))#gives the given value how many times it have been repeated
print(a+b,len(a+b))#concats the two tuples and gives the length of resultant tuple
print(e,len(e))#prints as two seperate tuples and gives the length
print(f,type(f))#prints the list f and gives its type
g=tuple(f)#converting of the list into tuple
print(g,type(g))#converts the f into tuple
print(sorted(h))#sorts the given tuple