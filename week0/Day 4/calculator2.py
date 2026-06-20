def calculate(a, b ,operator):
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                return "Error: Division by zero"
            else:
                return a / b
        case _:
            return "Error: Invalid operator"
        
def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")
    result = calculate(a, b, operator)
    print(f"Result: {result}")
main()