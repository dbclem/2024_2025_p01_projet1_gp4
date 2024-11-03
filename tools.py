
# print(hex(255)[2:])
# print(bin(255)[2:])


# def decimal_to_hexadecimal(decimal_number):
#     hexadecimal_number = ""
#     hex_digits = "0123456789ABCDEF"

#     while decimal_number > 0:
#         remainder = decimal_number % 16
#         hexadecimal_number = hex_digits[remainder] + hexadecimal_number
#         decimal_number //= 16

#     return hexadecimal_number

# # Exemple d'utilisation
# nombre_decimal = 31
# nombre_hexadecimal = decimal_to_hexadecimal(nombre_decimal)
# print(f"Le nombre décimal {nombre_decimal} en hexadécimal est : {nombre_hexadecimal}")


# def decimal_to_binary(decimal_number):
#     binary_number = ""

#     while decimal_number > 0:
#         remainder = decimal_number % 2  # Reste de la division par 2
#         binary_number = str(remainder) + binary_number  # Ajoute le reste au début de la chaîne
#         decimal_number //= 2  # Divise le nombre par 2

#     return binary_number

# # Exemple d'utilisation
# nombre_decimal = 10
# nombre_binaire = decimal_to_binary(nombre_decimal)
# print(f"Le nombre décimal {nombre_decimal} en binaire est : {nombre_binaire}")


# def bin_to_dec(init_number):
#     dec_number = 0


#     for i in range(len(init_number)):
#         bit = int(init_number[len(init_number) - 1 - i])  # On parcourt la chaîne de droite à gauche
#         dec_number = dec_number + bit * (2 ** i)  # Ajoute la valeur décimale correspondante

#     return dec_number

# # Exemple d'utilisation
# nombre_binaire = "11111111"
# nombre_decimal = bin_to_dec(nombre_binaire)
# print(f"Le nombre binaire {nombre_binaire} en décimal est : {nombre_decimal}")
