# change Shamsi to Miladi
def changeYears(day , mounth , year):
    myear = 0
    if mounth >= 10:
        if day >=10:
            myear = year + 622
    else:
           myear = year + 621

    print(f"You born in {myear} years.")   
     
while True:
    day = int(input("enter days of your birthday: "))
    mounth = int(input("enter mounths of your birthday: "))
    year = int(input("enter years of your birthday: "))

    changeYears(day , mounth , year)        