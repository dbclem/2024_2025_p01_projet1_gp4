from data import *
from tools import * 

def bin_dec_hex_to_bin_dec_hex (init_number, init_base, target_base): 
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


def ask_for_the_init_base() : 
    init_base = input(ask_for_init_base_text)
    while not (is_a_valid_base(init_base)) == True:
        init_base = input(ask_again_for_init_base_text)
    return init_base

def is_a_valid_base(chain):
    return chain in base 




def ask_for_the_target_base() :
    target_base = input(ask_for_target_base_text)
    while not (is_a_valid_base(target_base)) == True:
        target_base = input(ask_again_for_target_base_text)
    return target_base
    


