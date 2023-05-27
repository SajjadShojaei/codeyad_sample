class Car:
    
    cars_number = 0

    def __init__(self , name , model , color):
        self.name = name
        self.model = model
        self.color = color
        self.status = False
        Car.cars_number += 1

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
c2 = Car('Mersedes Benz' , 's500' , 'white')
c3 = Car('bently' , '1414' , 'Dark Green')

c1.starting()                                
c1.starting() 
c1.off()                               
c1.off()

print(Car.cars_number) # -> 3 ,beacuse we create 3 cars objects (c1, c2, c3) and calling init() func for 3.