#Q5 WAF that takes a number as an input and find its reverse and computes the sum of its digit.

def reverse(n):
    m,l=n,n
    s,r=0,0
    while m>0:                  #finding sum
        k=m%10
        s=s+k
        m=m//10
    for i in range(0,len(str(n))):                #reversing digit
        while l>0:
            k=l%10
            r=(r*10)+k
            break
        l=l//10
    print('Reversed Number = ',r)
    print('Sum of Digits = ',s)
print('*'*20+' Reverse the number and calculate the sum of its digits '+'*'*20)
n=int(input('Enter the Number:  '))
reverse(n)