from math import*

def numbers_left (n):
    return n % 2


def dec_to_bin (init_number) :
<<<<<<< HEAD
    bin_number = 0
=======
    bin_number = '0'
>>>>>>> dcd7644d1a807e021be0aafbedef6d1029127d59
    while init_number > 0:
        bin_number = str(numbers_left(init_number)) + bin_number
        init_number = init_number // 2
    return bin_number

print (dec_to_bin(91))
<<<<<<< HEAD
=======

>>>>>>> dcd7644d1a807e021be0aafbedef6d1029127d59
