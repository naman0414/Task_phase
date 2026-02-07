string = 'abcdabcdabcdabcd'
word=list(string)
z=len(word)
n = int(input("Enter the num: "))
if z/n%2==0:

    for i in range(0,z,n):
        # print(i)
        print(string[i:i+ n])
else:
    print("Not possible")

