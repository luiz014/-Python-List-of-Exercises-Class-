

class Car:
    def __init__(self,km_liter=0,qntfuel=0):
        self.km_liter=km_liter
        self.qntfuel=qntfuel
        
    def ride(self,distance=0):
        diff=distance/self.km_liter
        self.qntfuel=self.qntfuel-diff
        return self.qntfuel,diff

    def checkfuel(self):
        print(f'Liters left: {self.qntfuel}')

    def add_fuel(self,qnt=0):
        self.qntfuel=self.qntfuel+qnt
        return self.qntfuel
    
def main():

    km=int(input('How many km per liter your car does ? '))
    car1=Car(km)

    add=str(input('Do you want to fuel your car? [y/n] '))[0].lower()
    
    if add == 'y':
        qnt=int(input('How many? '))
        car1.add_fuel(qnt)
        car1.checkfuel()

    distance=int(input('How many km will take the trip?'))
    print(f'You will spend {car1.ride(distance)[1]} liters from your car')
    car1.checkfuel()
    
    
    
main()
        