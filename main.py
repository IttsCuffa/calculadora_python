import calculos

def usuario_calculo():

    operacion_usuario=input("Que operacion quiere realizar-Suma-Resta-Multiplicacion-Division").capitalize()

    if operacion_usuario == 'Suma':
        print('Que numeros quiero sumar?')
        num1=int(input('Ingrese el numero 1: '))
        num2=int(input('Ingrese el numero 2: '))
        calculos.sumar(num1,num2)
    elif operacion_usuario == 'Resta':
        print('Que numeros quieres restar? ')
        num1=int(input('Ingrese el numero 1: '))
        num2=int(input('Ingrese el numero 2: '))
        calculos.restar(num1,num2)
    elif operacion_usuario == 'Multiplicacion':
        print('Que numeros quieres multiplicar?')
        num1=int(input('Ingrese el numero 1 : '))
        num2=int(input('Ingrese el numero 2: '))
        calculos.multiplicar(num1,num2)
    elif operacion_usuario == 'Division':
        print('Que numeros quieres dividir?')
        num1=int(input('Ingrese el numero 1: '))
        num2=int(input('Ingrese el numero 2: '))
        calculos.dividir(num1,num2)

    else:
        print('error')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   usuario_calculo()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
