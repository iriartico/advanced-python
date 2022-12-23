from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):  # Permite que se pasen n cantidad de parámetros sin crear un error
        initial_time = datetime.now()
        func(*args, **kwargs)  # kwargs = keywords arguments
        finally_time = datetime.now()
        time_elapsed = finally_time - initial_time
        print("Transcurrieron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass


@execution_time
def sum(a: int, b: int) -> int:
    return a + b


@execution_time
def hello(name="Martin"): # Parámetros nombrados (KeyWords Arguments)
    print('Hola' + name)


random_func()
sum(2, 3)
hello("Farid")
