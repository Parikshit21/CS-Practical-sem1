#Q3 WAF that takes a number as an input from the user and compute its factorial.

def fact(n):
    k=1
    if n<0:
        print('Factorial of negative number is not defined.')
    elif n==0:
        print(n,'! = ',1)
    else:
        for i in range(1,n+1):
            k=k*i
        print(str(n)+'! = ',k)
        
n=int(input('Enter the Number:  '))
fact(n)