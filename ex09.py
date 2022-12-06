

class Point:
    def __init__(self,y=0,x=0):
        self.x=x
        self.y=y
        
    def show_point(self):
        print(f'The point is located at intersection of {self.x} base and {self.y} height')

class Rectangle:
    def __init__(self,height=0,base=0):
        self.height=height
        self.base=base
        
    def center(self):
        a=input('Do you want to know the center of rectangle? (y/n) ').lower()[0]
        if a == 'y':
            heightmid=self.height/2
            basemid=self.base/2
            print(f'The center of rectangle is located at intersection of {heightmid:.0f} height and {basemid:.0f} base')
        else:    
            return heightmid,basemid
        return heightmid,basemid
    
        
    
def main():
    height=float(input('What is it height of rectangle?  '))
    base=float(input('and base? '))
    rectangle1=Rectangle(height,base)
    x=rectangle1.center()
    point1=Point(x[0],x[1])
    point1.show_point()
    
    
main()