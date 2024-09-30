from data import *
from tools import * 

def bin_dec_hex_to_bin_dec_hex (init_number, init_base_verify, target_base_verify): 
    pass
    target_number = None
    return target_number

def do_the_job ():
    init_number = ask_for_the_init_number()
    init_base = ask_for_the_init_base()
    target_base = ask_for_the_target_base()
    target_number = bin_dec_hex_to_bin_dec_hex (init_number, init_base, target_base)

#assert bin_dec_hex_to_bin_dec_hex("101", 2, 10) == "5"














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
    return init_base


def ask_for_the_target_base() :
    target_base = input(ask_for_target_base_text)
    while not (is_a_valid_base(target_base)) == True:
        target_base = input(ask_again_for_target_base_text)
    return target_base


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
        return init_base_verify == 2
    
    elif is_dec(test_for_init_base):
        return init_base_verify == 10
    
    elif is_hex(test_for_init_base):
        return init_base_verify == 16


def interpret_target_base (): #interpret la target_base --> donc savoir si c'est un bin / dec / hex
    target_base_verify = 0
    test_for_target_base = ask_for_the_target_base()
    if is_bin(test_for_target_base) :
        return target_base_verify == 2
    
    elif is_dec(test_for_target_base):
        return target_base_verify == 10
    
    elif is_hex(test_for_target_base):
        return target_base_verify == 16



test = ask_for_the_init_number()+ ", " + ask_for_the_init_base()+ ", " + ask_for_the_target_base()
print(test)

#tout est reconnu et est pres a etre utilisé dans les calcules 
