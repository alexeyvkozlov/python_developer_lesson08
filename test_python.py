import math

def test_filter():
  # Тест для функции filter
  numbers = [1, 2, 3, 4, 5]
  filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
  assert filtered_numbers == [2, 4]

def test_map():
  # Тест для функции map
  numbers = [1, 2, 3, 4, 5]
  squared_numbers = list(map(lambda x: x**2, numbers))
  assert squared_numbers == [1, 4, 9, 16, 25]

def test_sorted():
  # Тест для функции sorted
  unsorted_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
  sorted_numbers = sorted(unsorted_numbers)
  assert sorted_numbers == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_math_pi():
  # Тест для константы pi из модуля math
  assert math.pi == 3.141592653589793

def test_math_sqrt():
  # Тест для функции sqrt из модуля math
  assert math.sqrt(25) == 5.0

def test_math_pow():
  # Тест для функции pow из модуля math
  assert math.pow(2, 3) == 8

def test_math_hypot():
  # Тест для функции hypot из модуля math
  assert math.hypot(3, 4) == 5.0
