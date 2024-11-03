from data import *
from tools import * 



def dec_to_hex (init_number):
    hex_number = ""
    hex_chars = "0123456789ABCDEF"
    while init_number > 0:
        point_hex_char = init_number % 16
        hex_number = hex_chars[point_hex_char] + hex_number
        init_number = init_number // 16
    return hex_number#--> marche 

def dec_to_bin(init_number):
    bin_number = ""
    while init_number > 0 :
        reste = init_number % 2
        bin_number = str(reste) + bin_number
        init_number = init_number // 2
    return bin_number #--> marche

def bin_to_dec(init_number):
    dec_number = 0
    for i in range(len(init_number)):
        bin_number = int(init_number[len(init_number) - 1 - i])  
        dec_number = dec_number + bin_number * (2 ** i)  
    return dec_number#--> marche

def bin_to_hex (init_number) : 
    return dec_to_hex(bin_to_dec(init_number)) #--> marche 

def hex_to_dec (init_number):
    dec_number = 0 
    hex_in_dec_chars = transforme_hex_number_to_dec_numbers(init_number)
    for num in range(len(hex_in_dec_chars)):
        hex_number = int(hex_in_dec_chars[len(hex_in_dec_chars) - 1 - num])  
        dec_number = dec_number + hex_number * (16 ** num)
    return dec_number#--> marche

def hex_to_bin (init_number) :
    return hex_to_dec(dec_to_bin(init_number)) #--> marche


def ask_for_the_init_number() : 
    init_number = input(ask_for_init_number_text) 
    while not (is_a_valid_number(init_number)) == True:
        init_number = input(ask_again_for_init_number_text)
    return init_number

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


def bin_dec_hex_to_bin_dec_hex (init_number, init_base_verify, target_base_verify): 
    if init_base_verify == 2 and target_base_verify == 10:
        return bin_to_dec(init_number)
    elif init_base_verify == 2 and target_base_verify == 16:
        return bin_to_hex(init_number)

    elif init_base_verify == 10 and target_base_verify == 2:
        return dec_to_bin(int(init_number))
    elif init_base_verify == 10 and target_base_verify == 16:
        return dec_to_hex(int(init_number))

    elif init_base_verify == 16 and target_base_verify == 2:
        return hex_to_bin(init_number)
    elif init_base_verify == 16 and target_base_verify == 10:
        return hex_to_dec(init_number) 
    else : 
        return init_number


def do_the_job ():
    init_number = ask_for_the_init_number()
    init_base = interpret_init_base()
    target_base = interpret_target_base()
    target_number = bin_dec_hex_to_bin_dec_hex (init_number, init_base, target_base)
    print(f"Le nombre {init_number} en base {init_base} est {target_number} en base {target_base} !")


do_the_job()

