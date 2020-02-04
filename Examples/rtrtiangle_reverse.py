n=int(input("Enter the number"))
for i in range(n):
    space=n-(i+1)
    for k in range(space):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
    
