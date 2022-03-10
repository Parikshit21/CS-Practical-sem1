#Q15 Write a menu driven program to perform the following function on a string. 
#a)	Find the length of a string. 
#b)	Return maximum of three string. 
#c)	Accept a string and replace or successive character with #. 
#d)	Find number of words in the given string.


def lenstr(data):
    return len(data)

def maxstr(l1,l2,l3):
    if l1>l2 and l1>l3 :
        return l1
    if l2>l3 and l2>l3 :
        return l2
    else:
        return l3

def replace(data):
    lst=data.split()
    for i in lst :
        word=''
        for j in range(len(i)) :
            if j%2==0 :
                word+=i[j]
            else:
                word+='#'
        print(word, end=' ')

def countwrd(data):
    total=0
    lst=data.split()
    for i in lst :
        if i.isalpha() :
            total+=1
    return total

print('*'*30+' String Works '+'*'*30)
print('''Choose the action: 
1. Find length of string 
2. Find max between 3 strings 
3. Replace successive char with #
4. Count no. of words in the string''')

o=int(input('Enter the no. of action:  '))
if o==1:
    data=str(input('Enter the string: '))
    print(lenstr(data))
elif o==2:
    l1=str(input('Enter String1: '))
    l2=str(input('Enter String2: '))
    l3=str(input('Enter String3: '))
    print(maxstr(l1,l2,l3))
elif o==3:
    data=str(input('Enter the string: '))
    replace(data)
elif o==4 :
    data=str(input('Enter string: '))
    print(countwrd(data))