#Q12 WAF that prints a dictionary where the keys are numbers 
# between one and five and the values are cube of the keys.

def dictcube():
    d=dict()
    for i in range(1,6):
        d[i]=i**3
    print(d)
dictcube()