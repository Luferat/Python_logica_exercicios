'''
Soma uma quantidade arbitrária de números
'''

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num # total = total + num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


