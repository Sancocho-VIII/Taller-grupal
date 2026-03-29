nums_guardados=[]
while True:
  try:
    nums = int(input("Números que vas a ingresar: "))
    if nums.is_integer():
      break
  except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")
for i in range(nums):
  while True:
    try:
      num=int(input(f"Número {i+1}: "))
      nums_guardados.append(num)
      break
    except ValueError:
      print("Entrada no válida. Por favor, ingresa un número entero.")
while True:
  try:
    num_buscar = int(input("Que numero desea buscar?"))
    if num_buscar.is_integer():
      break
  except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")
for indice, j in enumerate(nums_guardados):
  if j == num_buscar:
    print(f"El num {num_buscar} esta en la posicion {indice+1}")