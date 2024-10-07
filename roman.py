from math import*

def rest_number (n):
    return n % 2


def dec_to_bin (init_number) :
    bin_number = '0'
    while init_number > 0:
        bin_number = str(rest_number(init_number)) + bin_number
        init_number = init_number // 2
    return bin_number

print (dec_to_bin(91))
