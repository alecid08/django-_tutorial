# Variables

my_variable = "My string variable"
print(my_variable)
my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

my_into_to_str_variable = str(my_int_variable)
print(my_into_to_str_variable)
print(type(my_into_to_str_variable))

# Concatenacion de variables en un print
(print(my_variable,my_int_variable,my_bool_variable))

print("Este es el valor de:",my_bool_variable)

# Algunas Funciones del sistema
print(len(my_variable))

# Variables en una sola línea
name, surname, alias, age = "Alejandro", "Cid", "Ale", 17
print("mi nombre es:", name, surname, ".Tengo:", age, "años", ".Mia alias es:", alias)

# Imputs

"""
name = input("¿Cuál e tu nombre?")
age = input("¿Cual es tu edad?")
print(name)
print(age)
"""

 # Cambiamos su tipo
name = 17
age = "Alejandro"

print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi direccion"
address = 32
address = True
address = 1.5
print(address)

print(type(address))