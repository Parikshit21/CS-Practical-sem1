#Q8 WAF that finds the sum of first n odd terms and first n even terms.

def odd(n):         #sum of odd no
    return n*n
def even(n):       #sum of even no
    return n*(n+1)
def all(n):          #sum of natural no
    return int((n*(n+1))/2)


print('Choose the action: \n1. Sum of first n Odd numbers \n2. Sum of first n Even numbers \n3. Sum of first n natural numbers')
o=int(input('Enter the no. of action:  '))
n=int(input('Enter the Number of Terms (n):  '))
if n<0:
    print('Terms cannot be negative.')
else:
    if o==1:
        print('Sum of first',n,'odd numbers = ',odd(n))
    elif o==2:
        print('Sum of first',n,'even numbers = ',even(n))
    elif o==3:
        print('Sum of first',n,'natural numbers = ',all(n))
    else:
        print('Invalid Choice')