import math #pra usar a biblioteca math do python

def delta(a,b,c):
    delta = (b**2)-(4*a*c)
    return delta

def raizes(a,b,c,):
    #cria uma variável pra receber a função delta, e o delta recebe a,b,c, se não ele da erro
    d = delta(a,b,c)
    #rd = math.sqrt(d) #uma outra maneira de calcular a raiz quadrada
    rd = d**(1/2) #rd é raiz de delta, tu pode colocar o d**(1/2) dentro do x1 e x2 que da no mesmo
    x1 = ((-b) + rd)/(2*a)
    x2 = ((-b) - rd)/(2*a)
    return (x1, x2)


print(raizes(1,2,-3))
