def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def modulo(n1, n2):
    return n1 % n2
def quotient(n1, n2):
    return n1 // n2
def exponent(n1, n2):
    return n1 ** n2
operation = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
    '%' : modulo,
    '//' : quotient,
    '**' : exponent
}
def calculator():
    n1 = float(input("\nEnter the first number: "))
    print("\nYou can do the following operations:")
    for operators in operation:
        print(operators)
    should_continue = True
    while should_continue:
        symbol = input("\nPick an operator: ")
        if symbol not in operation:
            print("\nSorry, You have entered an INVALID OPERATION...!!\n")
            exit()
        n2 = float(input("\nEnter the next number: "))
        calculation = operation[symbol]
        answer = calculation(n1, n2)
        print(f"\n{n1} {symbol} {n2} = {answer}")
        result = input("\nDo you wissh to continue? Type 'yes' or 'no', and if you wish to start a new calculation type 'new': ").lower()
        if result == "yes":
            n1 = answer
        elif result == "new":
            calculator()
        else:
            should_continue = False
            print("\nThank You...!!")
            exit()
calculator()