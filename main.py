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


assert bin_dec_hex_to_bin_dec_hex("101", 2, 10) == "5"



















































































def ask_for_the_init_number() : 
    return input(ask_for_init_number_text)

def ask_for_the_init_base() : 
    return input(ask_for_init_base_text)


def ask_for_the_target_base() :
    return input(ask_for_target_base_text)

