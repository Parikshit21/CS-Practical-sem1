#Q4 WAF to generate The Fibonacci sequence till n terms.

def fibbo(n):
    a=0
    b=1
    if n<=0:
        print('Number of Terms cannot be 0 or less than 0')
    elif n==1:
        print('Fibonacci Series : 0')
    elif n==2:
        print('Fibonacci Series : 0 1')
    else:
        print('Fibonacci Series : 0 1 ',end='')
        for i in range(n-2):           #first two terms 0,1 are pre defined
            c=a+b
            print(c,end=' ')
            a,b=b,c
            
n=int(input('Enter the Number of terms:  '))
fibbo(n)