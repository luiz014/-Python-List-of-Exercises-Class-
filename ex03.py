

'''Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)

Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.'''

class Rectangle:
    
    def __init__(self,height=0,base=0):
        self.height=height
        self.base=base
        
    
    def change_value(self,height=0,base=0):
        self.height=height
        self.base=base
        
    def return_value(self):
        return self.height, self.base
    
    def calc_area(self):
        area=self.height * self.base
        return area
    
    def calc_perimeter(self):
        perimeter=(2*self.height)+(2*self.base)

def main():
    
    widthA=float(input('What is it the width local measures in meters? '))
    depthA=float(input('and depth? '))
    sideA=Rectangle(widthA,depthA)
    
    widthB=30
    depthB=30
    sideB=Rectangle(widthB,depthB)
    
    areaA=sideA.calc_area()
    areaB=sideB.calc_area()
    
    perimeterA=sideA.calc_perimeter()

    print(f'You will need {perimeterA}m of baseboard at least.')        
    print(f'The local has {areaA}m² and tile has {areaB/1000}m².')
    print(f'You will need {round(areaA/(areaB/1000))} tiles at least.')
    
        
main()    
        