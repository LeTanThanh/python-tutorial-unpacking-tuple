if __name__ == "__main__":
  # Reviewing Python tuples

  example_tuple = 1, 2
  print(example_tuple)

  example_tuple = (1, 2)
  print(example_tuple)

  example_tuple = ()
  print(example_tuple)

  example_tuple = tuple()
  print(example_tuple)

  example_tuple = 1,
  print(example_tuple)

  example_tuple = (1,)
  print(example_tuple)

  # Unpacking a tuple

  x, y = (1, 2)
  print(x, y)

  x, y, z = (10, 20, 30)
  print(x, y, z)

  numbers = 10, 20, 30
  print(numbers)
  print(type(numbers))

  # Using unpacking tuple to swap values of two variables

  x = 10
  y = 20
  print(f"x = {x}, y = {y}")

  x, y = (y, x)
  print(f"x = {x}, y = {y}")
