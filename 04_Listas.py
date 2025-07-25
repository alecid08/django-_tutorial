# Listas

my_list = list()
my_other_list = []
print(len(my_list))

my_list = [35, 17, 56, 45, 73, 17]
print(my_list)
print(len(my_list))

my_other_list = [17, 1.81, "Alejandro", "Cid"]
print(type(my_other_list))

my_list_book = [22, True, "Hola", [1, 2]]
print(my_list_book)
print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[-2])
print(my_other_list[-3])
# print(my_other_list[-5]) IndexError
# print(my_other_list[4]) IndexError

print(my_list.count(17)) # Return number of occurrences of value.
age, height, name, surname = my_other_list
print("Mi edad es", age, "años")
print(my_list + my_other_list)
#print(my_list - my_other_list) Index Error

my_list_change = "Hola Mundo"
print(my_list)
print(type(my_list))

my_other_list.append("Alejandro")
print(my_other_list)

my_other_list.insert(1, "Blue")
print(my_other_list)

my_other_list.remove("Blue")
print(my_other_list)



