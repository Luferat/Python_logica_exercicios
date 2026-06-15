def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for chave, valor in details.items():
    print(" • ", chave.capitalize() + ":", valor)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding", car = "Fusca")

'''
Adicione chaves e valores para aumentar a lista!
'''
