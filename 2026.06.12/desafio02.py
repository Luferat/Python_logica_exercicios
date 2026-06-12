'''
Desafio 02
Mostre a tabuada completa desde 0 x 0 até 10 x 10 usando while aninhado.
'''

print("\n\nSuper tabuada!\n----------------\n")
i = 1
while i <= 10:
  print(f"\n--- Tabuada de {i} ---\n")
  j = 0 
  while j <= 10:
    print(f"{i} x {j} = {i * j}")
    j += 1
  i += 1