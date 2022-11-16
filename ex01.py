

class Ball:
    
    def __init__(self,color=0,circ=0,material=0):
        self.color=color
        self.circ=circ
        self.material = material
        
        
    def changeColor(self):
        change=input(f'Do you want to change the current color {self.color}? [y/n] ').lower()
        
        if change == 'y':
            new_color=input('New color: ')
            self.color=new_color
        else:
            print(f'Alright,the color will continue {self.color}')    
    
    def showColor(self):
        print(f'The color is {self.color} ')
        
                
def main():
    ball01 = Ball("Black", 5, "metal")

    while True:
        ball01.showColor()
        ball01.changeColor()

        continueA = input("Continue? [y/n] ")
        continueA= continueA[0].lower()
        if continueA == "n":
            break

    ball01.showColor()


main()
        
        
        
        