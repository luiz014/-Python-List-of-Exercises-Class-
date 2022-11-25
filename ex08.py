

class Monkey():
    def __init__(self,name=str):
        self.name=name
        
        self.belly=[]
        
        
    def eat_food(self,fruit):
        self.belly.append(fruit)
        
        
    def see_belly(self):

        for food in self.belly:
            print(f'{food.name}: {food.qnt}')

        print('-'*30)
            
    
    def digest(self):
        total=0
        for food in self.belly:
            total=total+food.qnt
        return total


class Food():
    def __init__(self,name=str,qnt=0):
        self.name=name
        self.qnt=qnt
    
        
def main():
    monkey1=Monkey('Teddy')
    monkey2=Monkey('Homer')
    apple=Food('Apple',1)
    tomato=Food('Tomato',2)
    chesse=Food('Chesse', 3)
    foods=[]
    print(f'Monkey: {monkey1.name}')
    monkey1.eat_food(apple)  
    monkey1.see_belly()  
    monkey1.eat_food(tomato)
    monkey1.see_belly() 
    monkey1.eat_food(chesse)
    monkey1.see_belly() 
    print(f'Total: {monkey1.digest()}')
    print('-='*30)
    print(f'Monkey: {monkey2.name}')
    monkey2.eat_food(apple)  
    monkey2.see_belly()  
    monkey2.eat_food(tomato)
    monkey2.see_belly() 
    monkey2.eat_food(chesse)
    monkey2.see_belly() 
    print(f'Total: {monkey2.digest()}')


main()