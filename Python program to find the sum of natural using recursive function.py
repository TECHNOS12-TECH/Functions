n = int(input("Enter n natural numbers: "))

def add(n):
    if n<=1:
        return 1
    else:
        return add(n-1)+n
if n<0:
    print("Please enter positive value")
else:
    print("Required sum is",add(n))
        
