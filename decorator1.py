def mayus(func):
  def envelope(texto):
    return func(texto).upper()

  return envelope

@mayus
def message(name):
  return f'{name}, received a message'

print(message("Jorge"))