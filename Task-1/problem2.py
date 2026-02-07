word=input("Enter a string :")

sorted_str=list(word)
y=len(sorted_str)

for i in range(y-1):
    for j in range(y-i-1):
        if(sorted_str[j]>sorted_str[j+1]):
          sorted_str[j],sorted_str[j+1]=sorted_str[j+1],sorted_str[j]
          

sorted_word="".join(sorted_str)
print(sorted_word)