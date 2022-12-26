import time


def fibo_gen(max: int = None):
    n1, n2, counter = 0, 1, 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            if not max or aux <= max:
                n1, n2 = n2, aux
                counter += 1
                yield aux
            else:
                break


def run():
    fibonacci = fibo_gen(24)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)


if __name__ == '__main__':
    run()
