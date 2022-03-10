#Q2 WAP that reads an integer value and print leap year or not a leap year.

def ly(year):
    if year%400==0 :
        print(year,'is a Leap Year')
    elif year%100==0 :
        print(year,'is not a Leap Year')
    elif year%4==0 :
        print(year,'is a Leap Year')
    else:
        print(year,'is not a Leap Year')

year=int(input('Enter Year:  '))
ly(year)