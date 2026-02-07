def hill_num(n):
    num=len(list(n))
    for i in num(len/2-1):
        for j in i(len/2-i-1):
            if(num[j]>num[j+1]):
                num[j],num[j+1]=num[j+1],num[j]
                
    
       


num=int(input("Enter a number:"))
hill_num(num)
