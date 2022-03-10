#Q7 WAF that takes a number as an input and determine whether it is prime or not.

def prime(n):
    f=0
    if n<=0:
        print('Prime Number is defined only for Natural Numbers')
    elif n==1:
        print('1 is neither Prime nor Composite Number.')
    else:
        for i in range(2,int(n/2)+1):               #greatest no that can return integer on divide is its half
            if n%i==0:
                f=1
                break
        if f==0:
            print(n,'is a Prime Number.')
        else:
            print(n,'is not a Prime Number.')

n=int(input('Enter the Number :  '))
prime(n)