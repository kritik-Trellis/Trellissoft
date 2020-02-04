n=int(input("Enter the rows"))
for i in range(n,0,-1):
    space=n-i
    for k in range(space):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
