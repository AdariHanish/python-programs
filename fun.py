'''def d(dn):
  if dn == 0:
    return "0"
  b = ""
  while dn> 0:
    r= dn % 2
    b= str(r) + b
    dn //= 2
  return b
dn= int(input("enter the number:"))
b = d(dn)
print(f"{dn} in binary is: {b}")

def add(a,b):
  ans=a+b
  print(ans)
add(40,50)
def sum():
  n=int(input("enter the number:"))
  b=str(n)
  r = 0
  for i in b:
    r=r+(int(i)**3)
  print(r)
sum() 
a=0
n=int(input("enter the last series"))
for i in range(0,n):
  a=a+i
  print(a)'''
a=-1
b=1  
n=int(input("enter a number:"))
for i in range(0,n):
  res=a+b
  a=b
  b=res
  print(res)
