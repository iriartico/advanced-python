# Generador de números primos

import time


def is_prime(num: int) -> bool:
    counter: int = 0
    for i in range(1, num+1):
        if num % i == 0:
            counter += 1
    return counter == 2


def prime_gen(quantity: int = 1E+6):
    num, counter = 2, 0
    while True:
        number = is_prime(num)
        if number and counter < quantity:
            counter += 1
            yield num
        elif counter == quantity:
            break
        num += 1


def run():
    primes = prime_gen(10) # Especificar la cantidad de numeros primos
    for element in primes:
        print(element)
        time.sleep(1)


if __name__ == '__main__':
    run()
