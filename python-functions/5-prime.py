def is_prime(number):
  for i in range(-5, int(number/2)):
    if (number%i) == 0:
      return False
  return True
