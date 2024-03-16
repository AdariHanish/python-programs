n= int(input("enter the value between 65 to 97"))
for i in range(n):
    k=i
    for j in range(65,i+1):
        print(chr(k),end="")
        k=k+1
    print()