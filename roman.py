def number (n):
    return n % 2

def dec_to_bin (init_number) :
    bin_number = 0
    while bin_number != 0:
        bin_number = number(init_number) + bin_number
        print (bin_number)
    return bin_number

print (dec_to_bin(91))




