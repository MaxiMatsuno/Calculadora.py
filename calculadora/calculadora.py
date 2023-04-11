import sys

# Las variables se escriben con minusculas y una barra baja donde debería haber un espacio

# Agrega ': ' para mayor legibilidad
# Encierra las conversiones de int() en un try-except de ValueError
# ValueError salta cuando algo no se puede convertir a un entero de base 10
# Recoge la excepción y muestra un mensaje.

# La funcion input() recibe un string opcionalmente, que se imprime por pantalla 
# al pregunta, no te hace falta usar print

try:
    numero_1= int(input("Digame un numero: ")) 
except ValueError:
    print('Eso no es un numero!')
    sys.exit()

try:
    numero_2= int(input("Digame otro numero: "))
except ValueError:
    print('Eso no es un numero!')
    sys.exit()

# No ejecutes las operaciones antes de preguntarle al usuario, porque da igual que opcion
# elija, tu programa ya tendria hecho las 4 de antemano, lo cual no es eficiente.

# Agregado saltos de linea para un mensaje mas visual
print ("Dime que operacion hago:\n1) --> sumar\m2) --> multiplicar\n3) --> restar\n4) --> dividir")

# Agregado texto para ser mas visual y try-except
try:
    operador= int(input('Opcion: '))
except ValueError:
    print('Eso no es un numero!')
    sys.exit()

# Siempre usa if-elif-else. Esta estructura permite que, cuando python encuentra una 
# condición cierta, ejecuta el código que tiene debajo y luego deja de evaluar el resto 
# de la estructura if-elif-else. Si colocas siempre if, aunque el primero coincida, los 
# otros tres se evaluarán igualmente.
if operador == 1:
    print('{} + {} = {}'.format(numero1, numero2, numero_1 + numero_2))

elif operador == 2:
    print('{} - {} = {}'.format(numero1, numero2, numero_1 - numero_2))

elif operador == 3:
    print('{} * {} = {}'.format(numero1, numero2, numero_1 * numero_2))

elif operador == 4:
    print('{} / {} = {}'.format(numero1, numero2, numero_1 / numero_2))

# Añade el else para cualquier opcion no definida.
else:
    print('Operacion inválida!')