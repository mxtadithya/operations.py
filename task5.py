class calculator:
    def add(a,b):
        return(a+b)
    def subtract(a,b):
        return(a-b)
    def multiply(a,b):
        return(a*b)
    def divide(a,b):
        return(a/b)
    
calc=calculator
a=int(input("enter the 1st number"))
b=int(input("enter the 2st number"))

print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = input("Choose operation ")

if choice == "1":
    print( calc.add(a, b))
elif choice == "2":
    print( calc.subtract(a, b))
elif choice == "3":
    print( calc.multiply(a, b))
elif choice == "4":
    print( calc.divide(a, b))
else:
    print("Invalid choice")
