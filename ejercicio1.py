nums=[]
orden=["primer", "segundo", "tercer"]
utalio=1
while utalio==1:
	for i in zip(orden):
		try:
			num=int(input(f"Ingrese el {i} numero entero:"))
			if isinstance(num, int):
				nums.append(num)
			else:
				print("Error, ingresa un numero entero")
		except ValueError:
			print("Error, ingresa un numero entero")
	if isinstance(sum(nums), int)==True:
		utalio=0
	if len(nums)!=3:
		utalio =1
		nums.clear()
if utalio ==0:
	promedio = sum(nums)/len(nums)
	print(f"El promedio es {promedio}")

