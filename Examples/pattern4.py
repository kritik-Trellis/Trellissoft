n=int(input("Enter the rows"))
for i in range(n):
    space=i
    for k in range(space):
        print(end=" ")
    for j in range(n):
        if(i==0 or i==(n-1)):
            print("*",end="")
        else:
            if(j==0 or j==n-1):
                print("*",end="")
            else:
                print(end=" ")
    print()
