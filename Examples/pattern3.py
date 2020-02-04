n=int(input("Enter the rows"))
for i in range(n):
    space=n-(i+1)
    for k in range(space):
        print(end=" ")
    for j in range(n):
        print("*",end=" ")
    print()
