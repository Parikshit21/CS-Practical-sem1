#Q14 WAF called check_duplicats that takes a list and returns true 
#if there is any element that appears more than once. Also find a 
#frequency of that element. Original list should not be modified.

def check_duplicates(lst1):
    dupl={}
    count=0
    for i in lst1 :
        if i not in dupl :
             dupl[i]=1
        else:
            dupl[i]+=1
            count=1
    if count==1 :
        for i in dupl :
            if dupl[i]>1 :
                print(i,'occurs',dupl[i],'times')
        return True

l=list(map(str, input('Enter elements of the list separated by comma:  ').split(',')))
print(check_duplicates(l))