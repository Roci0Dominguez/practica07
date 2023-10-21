MaxTamC = 10
A = [0] * MaxTamC
frente = 0
final = 0
contador = 0

# Inicializar la cola
frente = 0
final = 0

respuesta = input("¿Desea agregar elementos a la cola? (s/n): ").lower()

while respuesta == 's' and contador < MaxTamC:  # Cambiado '< 0' a '< MaxTamC'
    if (final + 1) % MaxTamC == frente:
        print("Desbordamiento de cola")
        exit(1)

    elemento = int(input("Ingrese un elemento para la cola: "))  # Cambiado 'intput' a 'input'
    final = (final + 1) % MaxTamC
    A[final] = elemento

    contador += 1
    print(f"Elemento {contador} agregado a la cola: {elemento}")

    if contador < MaxTamC:  # Cambiado '< 10' a '< MaxTamC'
        respuesta = input("¿Desea agregar más elementos a la cola? (s/n): ").lower()

# Validar si la cola está vacía
if frente == final:
    print("La cola está vacía")

# Obtener el primer elemento de la cola
primerElemento = A[(frente + 1) % MaxTamC]
print(f"El primer elemento de la cola es: {primerElemento}")

# Eliminar el frente
frente = (frente + 1) % MaxTamC

# Imprimir elementos de la cola en el orden en que fueron ingresados
print("Elementos de la cola en el orden de ingreso: ")
i = (frente + 1) % MaxTamC
while i != (final + 1) % MaxTamC:
    print(A[i], end=" ")
    i = (i + 1) % MaxTamC
print()