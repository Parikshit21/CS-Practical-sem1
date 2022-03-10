#Q11 WAF that reads a text file and can calculates the frequency of 
#letters as a variable of dictionary type to maintain the count.

def freq():
    data=str(input('Enter sentence: '))
    d=dict()
    for ch in data:
        if ch in d :
            d[ch]+=1
        else:
            d[ch]=1
    print(d)


freq()