def sumar(num1,num2):

     resultado=num1+num2
     print(resultado)

def restar(num1,num2):

    resultado=num1-num2
    print(resultado)
def multiplicar(num1,num2):

    resultado=num1*num2
    print(resultado)
def dividir(num1,num2):

  try:
      resultado=num1/num2
  except ZeroDivisionError:
      print('No se puede dividir por cero')

  else:print(resultado)

