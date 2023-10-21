capacidad = 10
elementos = [0] * capacidad
tope = -1

print("Tecla elemento de la pila (termina con -1)")

x = 0
CLAVE = -1

while x != CLAVE:
    entrada = input()
    if entrada.isdigit():
        x = int(entrada)
        if tope < capacidad - 1:
            tope += 1
            elementos[tope] = x
        else:
            print("Excepcion: pila llena")
            break
    else:
        print("Excepcion: Entrada no valida")

# Print the elements of the stack
if tope >= 0:
    print("Elementos de la pila:")
    while tope >= 0:
        x = elementos[tope]
        tope -= 1
        print(x, end=" ")
    print()
else:
    print("Pila vacia")