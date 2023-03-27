import math

def prime_number(*numbers):
    for number in numbers:
        if(is_prime_number(number)):
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")

def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


prime_number(1,2,3,25,19,22)