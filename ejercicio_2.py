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
      num=float(input(f"Número {i+1}: "))
      nums_guardados.append(num)
      break
    except ValueError:
      print("Entrada no válida. Por favor, ingresa un número entero.")
  nums_guardados.append(num)
print(f"El mayor es: {max(nums_guardados)}")
print(f"El menor es: {min(nums_guardados)}")
