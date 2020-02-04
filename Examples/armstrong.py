#armstrong numbers b/w 100 and 999
for i in range(100,1000):
    sum=0
    cube=1
    num=i
    while num>0:
        c=num%10
        num=num//10
        cube=c*c*c
        sum=sum+cube
    if(i==sum):
        print(i)

    
