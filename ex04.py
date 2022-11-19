

class Person:
    def __init__(self,name=0,age=0,weight=0,height=0):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
           
        
    def fat(self,weight):
        self.weight=self.weight+weight
        print(f'You will have {self.weight} kg ')
            
    
    def loose(self,weight): 
        self.weight=self.weight-weight
        print(f'You will have {self.weight} kg ')
            
    
    def grow(self,centimeters):
        self.height=self.height+(centimeters/100)
        print(f'You grown up {self.height} m ')
        
    def aging(self,years):

        if self.age <21:
             self.height =self.height+(0.05*years)
       
        return self.height
                
    
    
def main():
    
    person1 = Person('Kyle', 12,80,1.80)
    print(f'Name: {person1.name}\nAge: {person1.age}\nWeight: {person1.weight}\nHeight: {person1.height}')

    earn=int(input('How many kg do you want to earn? '))
    person1.fat(earn)
    
    loose=int(input('How many kg do you want to loose? '))
    person1.loose(loose)
    
    grow=int(input('How many centimeters do you want to grow? '))
    person1.grow(grow)
    
    if person1.age < 21:
        years=int(input('How many years left until 21 years old? '))
        print(f'You will become {round(0.05*years)} taller. Total {person1.aging(years)} m')
    
    
main()
            
        
                         