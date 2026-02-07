n=int(input("Enter a number :"))
first=0
second=1
print("0 1",end=" ")
for i in range(2,n):
    sum=first+second
    second,first=sum,second
    print(sum,end=" ")
   

