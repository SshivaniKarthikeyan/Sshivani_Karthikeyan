#Electricity bill
#Author:Sshivani Karthikeyan
unit=float(input("Enter no of unit:"))
if(unit<=100):
    print("No electricity charge")
elif(unit>100 and unit<250):
    charge=unit*0.5
    print("Electricity bill is:",charge,"Rs")
elif(unit>250 and unit<400):
    charge=unit*5
    print("Electricity bill is:",charge,"Rs")
elif(unit>400 and unit<500):
    charge=unit*10
    print("Electricity bill is:",charge,"Rs")
elif(unit>=500):
    charge=unit*20
    print("Electricity bill is:",charge,"Rs")
else:
    print("Invalid amount")
