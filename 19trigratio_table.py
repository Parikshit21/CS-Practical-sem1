#Q19 WAP to produce a table of sins, cosines and tangents. Make a
#variable x in range from 0 to 10 in steps of 0.2. For each value
#of x, print the value of sin(x), cos(x) and tan(x).
import math as m
x=0
print('*'*30+' Table for Sine, Cosine and Tangent Values '+'*'*30)
print('Value\t\tSine\t\tCosine\t\tTangent')
while x<=10 :
    print('{}\t\t{}\t\t{}\t\t{}'.format(round(x,2),round(m.sin(x),4),round(m.cos(x),4),round(m.tan(x),4)))
    x+=0.2