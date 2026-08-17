#quadratic equation
a= int(input("Enter value for a:"))
b=int(input("Enter value for b:"))
c=int(input("Enter value for c:"))
B2=b**2
Z=4*a*c
W=B2-Z
rt=W*0.5*0.5
pos=(-b+rt)/(2*a)
neg=(-b-rt)/(2*a)
print("Value of quad when added:",pos)
print("Value of quad when sub:",neg)
