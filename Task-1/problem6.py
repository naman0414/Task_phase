def anangram(word1,word2):
    string1=list(word1)
    string2=list(word2)

    if len(word1)==len(word2):
        for i in string1:
            if(i in string2):
                string2.remove(i)
        if len(string2) == 0:
            print("Yes")
        else:
            print("It is not")
    else:
        print('It is not')
anangram('listen','silent')