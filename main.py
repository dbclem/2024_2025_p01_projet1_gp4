from data import *
from tools import * 

def bin_dec_hex_to_bin_dec_hex (init_number, init_base_verify, target_base_verify): 
    if target_number == 2 and target_base_verify == 10:
        target_number = bin_to_dec()
    elif target_number == 2 and target_base_verify == 16:
        target_number = bin_to_hex()

    elif target_number == 10 and target_base_verify == 2:
        target_number = dec_to_bin()
    elif target_number == 10 and target_base_verify == 16:
        target_number = dec_to_hex()

    elif target_number == 16 and target_base_verify == 2:
        target_number = hex_to_bin()
    elif target_number == 16 and target_base_verify == 10:
        target_number = hex_to_dec() 
           
    return target_number

#assert bin_dec_hex_to_bin_dec_hex("101", 2, 10) == "5"




def do_the_job ():
    init_number = ask_for_the_init_number()
    init_base = ask_for_the_init_base()
    target_base = ask_for_the_target_base()
    target_number = bin_dec_hex_to_bin_dec_hex (init_number, init_base, target_base)



def dec_to_hex (init_number):
    hex_number = ""
    hex_chars = "0123456789ABCDEF"
    while init_number > 0:
        point_hex_char = init_number % 16
        hex_number = hex_chars[point_hex_char] + hex_number
        init_number = init_number // 16
    return hex_number

def bin_to_hex (init_number) : 
    return dec_to_hex(bin_to_dec(init_number))

def bin_to_dec(init_number):
    dec_number = 0
    for i in range(len(init_number)):
        bin_number = int(init_number[len(init_number) - 1 - i])  
        dec_number = dec_number + bin_number * (2 ** i)  
    return dec_number

def dec_to_bin(init_number):
    bin_number = ""
    while init_number > 0 :
        reste = init_number % 2
        bin_number = str(reste) + bin_number
        init_number = init_number // 2
    return bin_number

def hex_to_dec (init_number) :
    dec_number = 0
    for i in range(len(init_number)):
        hex_number = int(init_number[len(init_number) - 1 - i])  
        dec_number = dec_number + hex_number * (16 ** i)  
    return dec_number  #--> correction ici pas fini

def dec_to_hex (init_number): 
    return bin_to_hex(dec_to_bin(init_number))

def hex_to_bin (init_number) :
    return hex_to_dec(dec_to_bin(init_number))













def check_char_number_validity(char):
    return char in hex_number_valid_chars

def is_a_valid_number(chain): 
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i <= len(chain) - 1:
        is_a_valid_char = check_char_number_validity(chain[i])
        i = i + 1
    return is_a_valid_char


def ask_for_the_init_number() : 
    init_number = input(ask_for_init_number_text) 
    while not (is_a_valid_number(init_number)) == True:
        init_number = input(ask_again_for_init_number_text)
    return init_number


def is_a_valid_base(chain):
    return chain in base 


def ask_for_the_init_base() : 
    init_base = input(ask_for_init_base_text)
    while not (is_a_valid_base(init_base)) == True:
        init_base = input(ask_again_for_init_base_text)
    return init_base # --> ici on voit a veréfié la validité de la base, mais l'ordi ne la connait


def ask_for_the_target_base() :
    target_base = input(ask_for_target_base_text)
    while not (is_a_valid_base(target_base)) == True:
        target_base = input(ask_again_for_target_base_text)
    return target_base # --> ici on voit a veréfié la validité de la target base, mais l'ordi ne la connait


def is_bin(chain):
    return chain in is_bin_writing

def is_dec(chain):
    return chain in is_dec_writing

def is_hex(chain):
    return chain in is_hex_writing

def interpret_init_base (): #interpret l'init_base --> donc savoir si c'est un bin / dec / hex
    init_base_verify = 0
    test_for_init_base = ask_for_the_init_base()
    if is_bin(test_for_init_base) :
        init_base_verify = 2
        return init_base_verify
    
    elif is_dec(test_for_init_base):
        init_base_verify = 10 
        return init_base_verify
    
    elif is_hex(test_for_init_base):
        init_base_verify = 16 
        return init_base_verify 


def interpret_target_base (): #interpret la target_base --> donc savoir si c'est un bin / dec / hex
    target_base_verify = 0
    test_for_target_base = ask_for_the_target_base()
    if is_bin(test_for_target_base) :
        target_base_verify = 2
        return target_base_verify
    
    elif is_dec(test_for_target_base):
        target_base_verify = 10
        return target_base_verify
    
    elif is_hex(test_for_target_base):
        target_base_verify = 16 
        return target_base_verify



# print(f"Vous avez choisi le nombre : ", ask_for_the_init_number()\
#     + " , en base : " + str(interpret_init_base()) \
#     + " , et vous visez la base : " + str(interpret_target_base()))


#tout est reconnu et est pres a etre utilisé dans les calcules 

