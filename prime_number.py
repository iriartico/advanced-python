# Crea un programa que verifique si un número es primo o no, pero hazlo con tipado estático.

def is_prime(num: int) -> bool:
    count: int = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count == 2


def run():
    num = input('Ingresa un número positivo: ')
    assert num.isnumeric() and int(num) > 0, 'Debe ingresar un número positivo'
    print(is_prime(int(num)))


if __name__ == '__main__':
    run()
