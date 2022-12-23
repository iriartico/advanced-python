# INPUT     OUTPUT
# Hola 3 -> HolaHolaHola
# Facundo 2 -> FacundoFacundo
# Platzi 4 -> PlatziPlatziPlatziPlatzi

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Debe ingresar cadenas de texto al repetidor"
        return string * n

    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("123"))


if __name__ == '__main__':
    run()
