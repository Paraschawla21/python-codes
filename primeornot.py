n = int(input("Enter the number you wish to check: "))
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print("It's a Prime Number")
    else:
        print("It's not a Prime Number")
prime_checker(number = n)