#Q9 WAF to produce given two patterns. 


def patterna(n):
    for j in range(1,n+1):                         #for rows
        for i in range(j,0,-1):                    #for columns
            print(i,end='')
        print()                                    #next line

n=int(input('Enter the no. of rows to be printed:  '))
patterna(n)


def patternb(h):
    n=h*2
    for i in range (1,n):          #no. of row
        if i<=h:                     #increasing pattern
            for j in range(h,i-1,-1):        #for spaces
                print(' ',end='')
            for j in range (1,i+1):          #for no.
                print(j,end='')
            for j in range (i-1,0,-1):
                print(j,end='')
            print()
        else:                         #decreasing pattern
            for j in range(h,i+1):           #for spaces
                print(' ',end='')
            for j in range(1,n-i+1):          #for no.
                print(j,end='')
            for j in range(n-i-1,0,-1):
                print(j,end='')
            print()

h=int(input("Enter the largest no of the Pattern:  "))
patternb(h)