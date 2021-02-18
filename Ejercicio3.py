##Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar
# (se ingresa un valor entero en el precio del producto)

precio=int(input("Digite el precio del producto "))
cantidad=int(input("Digite la cantidad a llevar "))
TotalPagar=precio*cantidad
print("La cantidad a pagar es ")
print(TotalPagar)