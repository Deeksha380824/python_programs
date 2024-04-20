print("1.add")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.square")
print("6.percentile")
print("7.//")
a=int(input("enter a number"))
b=int(input("enter second number"))
c=int(input("on the basis of above manu enter any number from 1 to 7"))
if c==1:
    ans=a+b
    print(ans)
elif c==2:
    ans=a-b
    print(ans)
elif c==3:
    ans=a*b
    print(ans)
elif c==4:
    ans=a/b
    print(a/b)
elif c==5:
    ans=a**b
    print(ans)
elif c==6:
    ans=a%b
    print(ans)
elif c==7:
    ans=a//b
    print(ans)    
