from typing import Dict, List, Tuple

positives: List[int] = [1,2,3,4,5]

users: Dict[str, int] = {
  'Argentina': 1,
  'Mexico': 2,
  'Brasil': 3,
}

countries: List[Dict[str, str]] = [
  {
    'name': 'Argentina',
    'people': '45000',
  },
  {
    'name': 'Mexico',
    'people': '23000',
  },
  {
    'name': 'Brasil',
    'people': '23467199',
  },
]

numbers: Tuple[int, float, int] = [1, 0.5, 2]

CoodinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoodinatesType = [
  {
    'coord1': (1,2),
    'coord2': (3,4)
  },
    {
    'coord1': (0,1),
    'coord2': (2,6)
  },
]

def run():
  print(positives)
  print(users)
  print(countries)
  print(numbers)
  print(coordinates)


if __name__ == '__main__':
  run()