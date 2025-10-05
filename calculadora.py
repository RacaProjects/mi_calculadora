def sumar(a: float, b: float) -> float:
    #Suma dos números.
    return print(f"Sumatoria de numeros", a + b)

def restar (a: float, b: float) -> float:
    #Resta el segundo número al primero.
    return print(f"Resta de numeros", a - b)

def multiplicar(a: float, b: float) -> float:
    #Multiplica dos números.
    return print(f"Multiplicacion de numeros", a * b)

def dividir(a: float, b: float) -> float:
   #Divide el primer número por el segundo.
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return print(f"Divicion de numeros", a / b )

def potencia(a: float, b: float) -> float:
    #Calcula a elevado a la b
    return print(f"elevacion de numeros", a**b)

def elevar_al_cubo(a:float, b:float) -> float:
    #Calculamos ambos numeros por separados
    num1_al_cubo = a ** 3
    num2_al_cubo = b ** 3
    return print(f"Elevacion al cubo de cada numero", a , b )

#Pediremos que el usuario digite dos numeros para hacerlo mas didactico

print ("Calculdora de dos numeros")
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))

print ("Escoge la operacion a realizar: ")
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicar")
print ("4. Divicion")
print ("5. Potenciacion")
print ("6. Elevacion al cubo de cada numero")
eleccion = int(input("Escribe solo el numero para escoger: "))

if eleccion == 1 :
    print(sumar(num1, num2))
elif eleccion == 2:
    print(restar(num1, num2))
elif eleccion == 3:
    print(multiplicar(num1, num2))
elif eleccion == 4:
    print(dividir(num1, num2))
elif eleccion == 5:
    print(potencia(num1,num2))
elif eleccion == 6:
    print(elevar_al_cubo(num1, num2))
    
