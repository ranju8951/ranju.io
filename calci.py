def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if y != 0:
        return x // y
    else:
        return "Error! Division by zero."
    
def mod(x,y):
    return x % y

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")

while True:
    choice = input("Enter choice: ")

    if choice in ['1', '2', '3', '4','5']:
        n = int(input("Enter first number: "))
        m = int(input("Enter second number: "))

        if choice == '1':
            print(n+m)
        elif choice == '2':
            print(n-m)
        elif choice == '3':
            print(n*m)
        elif choice == '4':
            print(n//m)
        elif choice == '5':
            print(n%m)
        
        nextcal = input("Enter 1 to continue 0 to exit: ")
        if nextcal.lower() != '1':
            break
    else:
        print("Invalid Input")
