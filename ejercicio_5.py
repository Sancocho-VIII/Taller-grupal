contador = 0
while True:
  try:
    num = int(input("Ingrese un numero entero positivo "))
    if num.is_integer():
        break
  except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")
while num>=1: 
    print(f"{num} / 2 = {num/2}")
    num /=2
    contador +=1
print(f"Se dividio {contador} veces")

  
  