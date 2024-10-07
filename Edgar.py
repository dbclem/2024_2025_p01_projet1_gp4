from math import*

def dec_to_hex_calcul (ask_for_the_init_number):
     return ask_for_the_init_number % 16


def dec_to_hex (init_number):
    hex_number = '0'
    while init_number > 0 :
         hex_number = str(dec_to_hex_calcul(init_number)) + hex_number
         init_number =  init_number // 2       
    return hex_number

print (dec_to_hex(91))