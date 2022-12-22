def is_palindrome(string: str) -> bool:
  string = string.replace(' ','').lower()
  return string == string[::-1]

def run():
  string = input('Ingrese una palabra: ')
  assert len(string) > 0, 'No se puede ingresar cadenas vacías'
  assert not string.isnumeric(), 'No se puede ingresar números'
  print(is_palindrome(string))

if __name__ == '__main__':
  run()