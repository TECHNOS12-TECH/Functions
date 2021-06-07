# Return maximum of three numbers using functions

a=int(input("Enter value of first number: "))
b=int(input("Enter value of Second number: "))
c=int(input("Enter value of Third number: "))
pass 
def maximum(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
m = maximum(a,b,c)
print("The greatest of three numbers is:",m)
