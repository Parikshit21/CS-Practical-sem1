#Q6 WAF that takes two number as an input parameter and returns their LCM.

def lcm(n1,n2):
    if n1<=0 or n2<=0 :
        print('LCM is defined only for Natural Numbers.')
    else:
        if n1>n2:
            ger=n1
        else:
            ger=n2
        while(True):
            if ger%n1==0 and ger%n2==0 :
                print('LCM of',n1,'and',n2,'is',ger)
                break
            ger+=1

n1=int(input('Enter the first number:  '))
n2=int(input('Enter the second number:  '))
lcm(n1,n2)