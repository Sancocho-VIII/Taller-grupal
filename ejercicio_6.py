import time
while True:
    entrada_cantidad = input("¿Cuántos números desea ingresar? ")
    if entrada_cantidad.isdigit():
        n = int(entrada_cantidad)
        if n > 0:
            break
        else:
            print("Por favor, ingrese un número mayor a 0.")
    else:
        print("Error: Debe ingresar un número entero válido.")
numeros = []
for i in range(n):
  while True:
    try:
      num = float(input(f"Número {i+1}: "))
      numeros.append(num)
      break
    except ValueError:
      print("Error: Debe ingresar un número entero válido.")
print("Parejas de números:")
time.sleep(1)
for i in range(len(numeros)):
  for j in range(len(numeros)):
    if i!=j:
      print(f"({numeros[i]}, {numeros[j]})")
      time.sleep(1)