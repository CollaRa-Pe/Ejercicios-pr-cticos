def calculadora():
#función que calcula una operación pidiendo los números y la operación a realizar al usuario
    try: #bloque try-except para validar que se entren números
        primer_número = int(input("Inrroduce el primer número, por favor: "))
        segundo_número = int(input("Introduce el segundo número, por favor "))
        operacion_a_realizar = input("Introduce la operación que quieres realizar: ")
        #bloque if-elif-else para aplicar operador válidos a los números dados. 
        if operacion_a_realizar == "+":
            print(primer_número + segundo_número)
        elif operacion_a_realizar == "-":
            print(primer_número - segundo_número)
        elif operacion_a_realizar == "*":
            print(primer_número * segundo_número)
        elif operacion_a_realizar == "/":
            try: #bloque try except para validar que no se divida por 0
                print(primer_número/segundo_número)
            except ZeroDivisionError:
                print("No es posible dividir por 0")
        else: 
            print("Debes entrar un operador de operaciones válido: +, -, * o /")
    except ValueError:
        print("Es necesario introducir un número")
