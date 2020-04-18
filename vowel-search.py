
def vowel_search(size):
    lis=[]
    for x in range(0,size):
        lis.append(input())

    vowels="aeiouy"
    count = "\n answer: \n"
    
    for string in lis:
        vowelcount=0
    
        for alpha in string:
            if alpha in vowels:
                vowelcount+=1
        
        if(vowelcount>0):
            count+=str(vowelcount)+"  "


    print(count)


vowel_search(int(input("Enter the number of string:\n")))
