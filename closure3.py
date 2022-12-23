# Generar un divisor anidado con closures

def make_division_by(n):
    def division(x):
        assert n != 0, "Error division by zero"
        return x // n
    return division


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(25))  # The expected output is 5

    division_by_10 = make_division_by(10)
    print(division_by_10(180))  # The expected output is 18
  
    division_by_0 = make_division_by(0)
    print(division_by_0(24))  # The expected output is Error


if __name__ == '__main__':
    run()
