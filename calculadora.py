def sumar(a: float, b: float) -> float:
    #Suma dos números.
    return a + b

def restar (a: float, b: float) -> float:
    #Resta el segundo número al primero.
    return a - b

def multiplicar(a: float, b: float) -> float:
    #Multiplica dos números.
    return a * b

def dividir(a: float, b: float) -> float:
   #Divide el primer número por el segundo.
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def potencia(a: float, b: float) -> float:
    #Calcula a elevado a la b
    return a**b


#Pediremos que el usuario digite dos numeros para hacerlo mas didactico

print ("Calculdora de dos numeros")
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero"))

if __name__ == "__main__":
    print(sumar(num1, num2))
    print(restar(num1, num2))  
    print(multiplicar(num1, num2))    
    print(dividir(num1, num2))       
