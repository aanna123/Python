
def simplecalc(x,y,choice):
    if choice=='+':
        return x+y
    elif choice=='-':
        return x-y
    elif choice=='*':
        return x*y
    elif choice=='/':
        return x/y
    elif choice=='%':
        return x%y
    elif choice=='//':
        return x//y
x, y = map(float, input("Enter two numbers separated by a space: ").split())
choice = input("Enter the operator (+, -, *, /, //, %): ")

# Calculating the result
result = simplecalc(x,y,choice)

# Printing the result
print(f"The result of {x} {choice} {y} is: {result}")
