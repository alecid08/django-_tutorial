## Strings ##

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)
 
my_new_line_string = "Este es un String \n con salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado "
print(my_scape_string)

my_scape_string = "\\tEste es un String \\n escapado "
print(my_scape_string)
 
# Formateo
name, surname, age = "Alejandro", "Cid", 17
print("Mi nombre es {} {} y mi edad es {} ".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d " %(name, surname, age))

print("Mi nombre es {name} {surname} y mi edad es {age}")

print(f"Mi nombre es {name} {surname} y mi edad es {age}")

 # Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)

# División
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)
# Reverse

reversed_language = language[::-1]
print(reversed_language)

language_slice = language[1:2:4]
print(language_slice)
language_slice = language[0:6:2]
print(language_slice)

# Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
