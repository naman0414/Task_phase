def triple_and(p1,p2,p3):
    if(p1 and p2 and p3):
        print("True")
    

num2=2
num1=8
p1=10
p2=16
p3=4

s1=num1+num2
s2=num1-num2
s3=num1/num2

if(s1==p1 and s2==p2 and s3==p3):
    triple_and(p1,p2,p3)
else:
    print("False")
