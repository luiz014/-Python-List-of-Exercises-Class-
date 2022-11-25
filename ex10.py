
class Pump():
    def __init__(self,name=0,typefuel=0,litervalue=0,qntfuel=0):
        self.name=name
        self.typefuel=typefuel
        self.litervalue=litervalue
        self.qntfuel=qntfuel    
   
    def fill_value(self,value):
        totalfuel=(1*value)/self.litervalue
        self.qntfuel=self.qntfuel-totalfuel
        return totalfuel,self.qntfuel
        
    def fill_fuel(self,liter):
        totalvalue=liter*self.litervalue
        self.qntfuel=self.qntfuel-liter
        return totalvalue,self.qntfuel
    
    def change_typefuel(self,fuel):
        self.typefuel=fuel
        return self.typefuel
    
    def change_litervalue(self,value):
        self.litervalue=value
        return self.litervalue
    
    def change_qntfuel(self,qnt):
        self.qntfuel=qnt
        return self.qntfuel
    
    def pump_status(self):
        print(f'{self.name} still have {round(self.qntfuel,2)} liters of {self.typefuel} and cost {self.litervalue} bucks per liter')
    
    
def main():
    
    pumpA=Pump('pumpA','Gasoline',3.5,50)
    value=float(input('How much do you want to pay to fuel your vehicle? '))
    a=round(pumpA.fill_value(value)[0],2)
    print(f'You filled with {a} liters in your vehicle')
    pumpA.pump_status()
    
    liters=float(input('How many liters do you want to fill your vehicle? '))
    b=round(pumpA.fill_fuel(liters)[0],2)
    print(f'Will cost to you {b} dolars')
    pumpA.pump_status()
    
    pumpA.change_litervalue(5)
    pumpA.change_qntfuel(100)
    pumpA.change_typefuel('Diesel')
    
    pumpA.pump_status()
    
main()