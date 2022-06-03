for numbers in range(1, 101):
    if numbers % 3 == 0:
        if numbers % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif numbers % 5 == 0:
        if numbers % 3 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(numbers)