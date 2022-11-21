

class VirtualMonster:
    def __init__(self,name=str,age=0,health=0,hungry=0):
        self.name=name
        self.age=age
        self.health=int(health)
        self.hungry=int(hungry)      

    def humor(self):
        humor=self.health+self.hungry
        if humor <100:
            humor_status='Bad'
        if humor >=100:
            humor_status='Good'
        return humor_status
                    
    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nHealth: {self.health}\nHungry: {self.hungry}'.format(self=self)
                
def main():
    vm=VirtualMonster('Jacky',1,50,50)
    print(vm) 
    print(f'Humor: {vm.humor()}')
 
main()
        