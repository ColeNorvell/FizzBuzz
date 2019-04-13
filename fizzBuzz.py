number = 1
while number <101:
    if number % 3 > 0 and number % 5 > 0:
        print(str(number))
    elif number % 3 == 0 and number % 5 > 0:
        print("Fizz")
    elif number % 3 > 0 and number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    number = number + 1
