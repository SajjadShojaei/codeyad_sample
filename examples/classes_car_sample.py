class Car:
    
    def __init__(self , name , model , color):
        self.name = name
        self.model = model
        self.color = color
        self.status = False

    def starting(self):
        if self.status == False:
            self.status = True
            print(f" Your {self.name} has been start ")
        else:
            print(f"Your {self.name} is already start , Don't Start again.")

    def off(self):
        if self.status == True:
            self.status = False
            print(f"Your {self.name} has been off")
        else:
            print(f"Your {self.name} is off, Please starting first.")

c1 = Car('LandRover' , 'Defender' , 'Black')
c1.starting()                                
c1.starting() 
c1.off()                               
c1.off()                               