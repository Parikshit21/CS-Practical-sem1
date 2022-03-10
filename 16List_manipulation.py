#Q16 WAP to perform the following using list. 
#a)	Check if all elements in list are numbers or not.
#b)	If it is numeric list then count number of odd values in it. 
#c)	If list contains all elements as strings, then display largest string in the list. 
#d)	Display list in reverse form. 
#e)	Find a specified element in the list. Remove the specified element.


def perform(lst,find,remv):

    try:
        sum(lst)
        print('All elements of the list are Numeric.')
        odd=0
        for i in lst:
            if i%2!=0 :
                odd+=1
        print(f'List has {odd} odd numbers.')
    except Exception:
        print('All elements of List are not Numbers.')
        
    flag=0
    for i in lst :
        if type(i)==str :
            continue
        else:
            flag=1
            break
    if flag==0 :
        print('All elements of the list are string')
        print(max(lst))
    else:
        print('All elements of the list is not string.')

    print(lst[::-1])

    if find in lst :
        ind=lst.index(find)
        print(f'{find} is present at index {ind}.')
    else:
        print(f'{find} is not present in the given list.')

    if remv in lst :
        lst.remove(remv)
        print(f'{remv} is removed from the list.')
    else:
        print(f'{remv} is not present in the given list.')

lst=['hi','tesla','salmon bhai','ukrain','pgdav']
find='salmon bhai'
remv='ukrain'
perform(lst,find,remv)
