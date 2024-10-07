from math import*

def rest_number (n):
    return n % 2


def dec_to_bin (init_number) :
    bin_number = '0'
    while init_number > 0:
        bin_number = str(rest_number(init_number)) + bin_number
        init_number = init_number // 2
    return bin_number

print (dec_to_bin(17))


def bin_to_dec (n, b):
    dec_number = 0
    for i in range (len(n)):
        dec_number =  dec_number + n[ len(n) - i - 1 ] * b ** i
    return dec_number

print (bin_to_dec (10100, 2))
