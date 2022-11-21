

class TV:
    def __init__(self,volume=0,channel=0):
        self.volume=volume
        self.channel=channel
        
    def highVolume(self,value):
        self.volume=self.volume+value
        return self.volume
        
        
    def lowVolume(self,value):
        self.volume=self.volume-value
        return self.volume
    
    def showStatus(self):
        print(f'Volume : {self.volume} and Channel: {self.channel}')
            
    def errorVolume(self):
        print('Volume should not surpass 0% or 100%')
        
    def errorChannel(self):
        print('Channel should be between 1 and 10')
                

def main():
    tvA=TV(0,0)
    #choose channel
    while True:
        channel=int(input('Which channel would you like? '))
        if 0<=channel<=10:
            tvA=TV(0,channel)
            break
        else:
            tvA.errorChannel()       
    #change volume
    while True:
    
        volume= str(input(f'Do you want to increase or decrease volume?\n[a]Increase\n[b]Decrease\n'))[0].lower()
        percent = int(input('How many percent? '))
        
        volume_conditional=int(tvA.volume)
        if 0<=percent<=100:
            if volume =='a':
                tvA.highVolume(percent)
                if not 0<=volume_conditional<=100:
                    tvA.errorVolume()
                    
            if volume =='b':
                tvA.lowVolume(percent)
                if not 0<=volume_conditional<=100:
                    tvA.errorVolume()
        else:
            tvA.errorVolume()
        tvA.showStatus()  
            
        
        a=input('Do you want to continue increase or decrease ? [Y/N] ')[0].lower()
        if a=='n':
            break    

main()