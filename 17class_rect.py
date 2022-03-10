#Q17 WAP to implement a class for finding area and perimeter of a
# rectangle. Write constructor, destructor and functions for 
#calculating area and perimeter.


from mimetypes import init
class rectangle():
    '''Rectangle as a class'''
    
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        a=self.length*self.breadth
        print(a)
    def perimeter(self):
        p=2*(self.length+self.breadth)
        print(p)

r=rectangle(10,3)
r.area()
r.perimeter()