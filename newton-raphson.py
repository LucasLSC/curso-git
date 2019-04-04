#             Metodo de Newton-Raphson

# importa o modulo math e a biblioteca sympy
from sympy import *
init_printing()
import math

x = symbols('x') #define x como variável simbólica.


def f(x):
  return x**3 - 9*x + 3 #cria a função f(x)

def derivada(funcao):
  return diff(f(x),x) #derivada da função f(x)

def newton_raphson(x0):
  interações = 5 #int(input("Digite o máximo de interações: "))
  i = 0
  precisao1 = 0 #float(input("Precisão 1: "))
  precisao2 = 1 #float(input("Precisão 2: "))
  
  while i < interações:
    print('\n')
    print('x{} = {}'.format(i, x0))
    func = f(x0) #func recebe a função f(x0) e calcula o resultado
    deriv = derivada(func) #deriva a func em função de x
    deriv = deriv.subs(x,x0) #substitui o x pelo valor do x0 e calcula o resultado
    print('função f(x) = ', func)
    print("f'(x) = ", deriv)
    y = float(x0 - (func/deriv)) #metodo de newton raphson
    print("x{} = {}".format(i+1, y))
  
    if (math.fabs(func) < precisao1 or (math.fabs(y - x0)) < precisao2):
      x0 = y
    i += 1

x0 = 1 #float(input('Digite o valor do  x inicial: '))
newton_raphson(x0)
