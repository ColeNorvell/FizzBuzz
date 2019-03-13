'''Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.'''

x = 1

while x <= 100:
    fizz = x % 3
    buzz = x % 5
    if fizz != 0 and buzz != 0:
        print(x)
    elif fizz == 0 and buzz != 0:
        print("Fizz")
    elif fizz != 0 and buzz == 0:
        print("Buzz")
    elif fizz == 0 and buzz == 0:
        print("FizzBuzz")
    x = x + 1
