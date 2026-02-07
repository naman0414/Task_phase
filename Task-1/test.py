
# name=input("enter name:")
# print(name)

# num1=int(input("enter number:"))
# num2=int(input("enter number:"))
# print(num1+num2)

# stndrd=int(input("enter standard:"))
# print(stndrd)

# print("i study in "+str(stndrd)+ " and my name is "+name)



# lst=["naman","idant","aryan"]
# length=len(lst)
# for i in range(0,length):
#     print(lst[i])


# for i in lst:
#     for j in i()
#     print(i)


# fibonacci
# first=0
# second=1
# n=int(input("enter till where you want the series :"))
# print(first,second,end=" ")
# for i in range(2,n+1):
#      s=first+second
     
#      first=second
#      second=s
#      print(s,end=" ")


# palindrome-
# name=str(input("enter a name: ").lower())
# n=name[ : :-1]

# if n==name:
#     print("palindrome")
# else:
#     print("not a palindrome")

# sum of digits of a num--


# n=int(input("enter number :"))
# s=0
# while(n!=0):
#     rem=n%10
#     s=s+rem
#     n=n//10

# print(s)


# find largest of three numbers--

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=int(input("enter third number:"))

# if a>=b and a>=c:
#     print("a is greatest")

# elif b>=a and b>=c:
#     print("b is greatest")
# else:
#     print("c is grestest")


# multiplication table:

# n=int(input("enter n :"))
# print("The table of "+str(n)+ " is :" )
# for i in range(1,11):
#     print(str(n)+"x"+str(i)+"="+str(n*i))

# vowels in a string:=
# count=0
# vowel={"a","e",'i',"o","u"}
# word=input("enter a word: ").lower()
# for i in range(0,len(word)):
#     if word[i] in vowel:
#         count=count+1
        
        
# print(count)

# arr=[1,2,6,53,3]
# arr.append(34)
# print(arr)

secret_word="giraffe"
i=0
guess=""
while(i<3):

    guess=input("enter secret word :")
    i=i+1 
    if(guess==secret_word):
      print("you win")
      break

    else:
      print("try again")
      continue






