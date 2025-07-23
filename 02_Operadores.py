# Operadores Aritméticos 
 # Operador (+) # Suma
r = 3 + 2
print(r) # r = 5
print(type(r)) # podemos comprobarlo con la función type

 # Operador (-) # Resta
a = 4-7
print(a) # a = -3
print(type(a)) # podemos comprobarlo con la función type

 # Operador (-) # Negación
b = -7 
print(b) # b = -7
print(type(b)) # podemos comprobarlo con la función type

 # Operador (*) # Multiplicación
c = 2*6 
print(c) # c = 12
print(type(c)) # podemos comprobarlo con la función type

 # Operador (**) # Exponente
d = 2**6 
print(d) # d = 64
print(type(d)) # podemos comprobarlo con la función type

 # Operador (/) # División
e = 3.5 / 2  
print(e) # r es 1.75
print(type(e)) # podemos comprobarlo con la función type

 # Operador (//) # División entera 
f = 3.5 // 2  
print(f) # r es 1.0
print(type(f)) # podemos combrobarlo con la funcion type

 # Operador (%) # Módulo
g = 7 % 2
print(g) # r es 1
print(type(g)) # Podemos comprobarlo con la funcion type

'''
El operador de módulo no hace otra cosa que devolvernos el resto de la división entre los dos operandos. 
En el ejemplo, 7/2 sería 3, con 1 de resto, luego el módulo es 1.
'''

print("Hola " + "Python " + "¿Que tal? ")
print("Hola " + str(5))
print("Hola " * (2**3))
my_float = 2.5 * 2
print("Hola " * int(my_float))

# Operadores Comparativos
print(3 > 4)
print(3 < 4)





# Operadores Logicos
'''
El operador and (&), del inglés “y”, devuelve 1 si el primer bit operando
es 1 y el segundo bit operando es 1. Se devuelve 0 en caso contrario.
'''
 # Operador (&) # (and)
h = 3 & 2  
print(r) # r es 5
'''
El operador or (|), del inglés “o”, devuelve 1 si el primer operando es 1
o el segundo operando es 1. Para el resto de casos se devuelve 0.
'''
 # Operador (|) # (or)
i = 3 | 2 
print(i) # r es 3
'''
El operador xor u or exclusivo (^) devuelve 1 si uno de los operandos
es 1 y el otro no lo es.
'''
 # Operador (^) # (xor)
j = 3 ^ 2  
print(j) # r es 1
'''
El operador not (~), del inglés “no”, sirve para negar uno a uno cada
bit; es decir, si el operando es 0, cambia a 1 y si es 1, cambia a 0.
'''
 # Operador (~) # (not)
k = ~3  
print(k) # r es -4 
'''
Por último los operadores de desplazamiento (<< y >>) sirven para
desplazar los bits n posiciones hacia la izquierda o la derecha.
'''
 # Operador (<<) # (Desplazamiento izq)
l = 3 << 1  
print(l) # r es 6

 # Operador (>>) # (Desplazamiento der) 
m = 3 >> 1
print(m) # m es 1

print(len("aaa") > len("aaaa")) # Cuenta Caracteres

# Operadores Logicos
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 and "Hola" < "Python")
print(not(3 < 4))

