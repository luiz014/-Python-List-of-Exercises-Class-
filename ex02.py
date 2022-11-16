

class Square:
    def __init__(self,side):
        self.side=side
        
    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self,value):
        if value.isdigit():
            self._side=value
        else:
            print('The value must be only in numbers')          
            
    def changeValue(self):
        new_value=int(input(f'Change value : {self._side} to : '))
        self._side=new_value

    def showValue(self):
        print(f'Current value is: {self._side}')
  
    def calculateArea(self):
        area=float(self._side)*float(self._side)
        print(f'The area of square is: {area}') 
        return area   
        
    def __str__(self):
        return f'The square have a side: {self._side} cm and area: {float(self._side)*float(self._side)} cm²' 
             
def main():
    
    side=input('Insert side value : ')
    square1=Square(side)
    square1.showValue()
    
    while True:

        a=input('Do you want to calculate the area? [y/n]')[0].lower()
        if a == 'y':
            square1.calculateArea()
            
        else:
            break
        
    print(square1)
    
main()

        
        
    
        
   