str="gautham is a coder"
count=0
vowel="a,e,i,o,u,A,E,I,O,U"
for i in str:
    if i in vowel:
        count = count+1
print("no of vowels",count)    