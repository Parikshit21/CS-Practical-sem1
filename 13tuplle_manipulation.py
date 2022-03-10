#Q13 Consider a tuple T1. Write a program following operation: - 
#a)	print half the values of tuple in one line and other half in the next line. 
#b)	Print another tuple whose values are even numbers in the given tuple. 
#c)	Concatenate a tuple T2 with T1. 
#d)	Return maximum and minimum value from this tuple.


t1=(1,2,5,7,9,2,4,6,8,10)

#part(a)
print('*'*30+' Print half tuple in two lines '+'*'*30)
for i in range(0,int(len(t1)/2)):
    print(t1[i],end=' ')
print()
for i in range(int(len(t1)/2),int(len(t1))):
    print(t1[i],end=' ')
print()

#part(b)
print('*'*30+' Print even no. '+'*'*30)
t3=()
for i in t1 :
    if i%2==0 :
        t3+=(i,)
print(t3)

#part(c)
print('*'*30+' Concatenating two tuples '+'*'*30)
t2=(11,13,15)
t1+=t2
print(t1)

#part(d)
print('*'*30+' Finding Max Min in the tuple '+'*'*30)
print(max(t1))
print(min(t1))