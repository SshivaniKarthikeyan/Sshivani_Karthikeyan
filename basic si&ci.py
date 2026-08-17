#S.I&C.I
principle=float(input("Enter principle amount:"))
rate=float(input("Enter rate of interest:"))
time=float(input("Enter time period of intrest:"))
SI=(principle*rate*time)/100
CI=((principle*(1+rate/100))**time)-principle
print("simple interest is:",SI)
print("compound interest is:",CI)
