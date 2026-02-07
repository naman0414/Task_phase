def selection_sort(word1):
    count=len((word1))
    word=list(word1)
    for i in range(count-1):
        for j in range(i+1,count-i-1):
            min_i=i
            if(word[j]<word[j+1]):
                word[j]

word=input('enter a string :')
print(selection_sort(word))

        