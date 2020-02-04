n=int(input("Enter the rows"))
for i in range(n):
    space=i
    for k in range(space):
        print(end=" ")
    for j in range(n-i): 
        print("*",end="")
    print()
