from data import*


def transforme_hex_number_to_dec_numbers (hex_number) : 
    hex_number_transformed_in_liste = []
    for i  in hex_number : 
        if i in "0123456789" : 
            hex_number_transformed_in_liste.append(int(i))
        else : 
            if i == "A" : 
                hex_number_transformed_in_liste.append(10)
            elif i == "B" : 
                hex_number_transformed_in_liste.append(11)
            elif i == "C" : 
                hex_number_transformed_in_liste.append(12)
            elif i == "D" : 
                hex_number_transformed_in_liste.append(13)
            elif i == "E" : 
                hex_number_transformed_in_liste.append(14)
            elif i == "F" : 
                hex_number_transformed_in_liste.append(15)                
    return hex_number_transformed_in_liste


def check_char_number_validity(char):
    return char in hex_number_valid_chars

def is_a_valid_number(chain): 
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i <= len(chain) - 1:
        is_a_valid_char = check_char_number_validity(chain[i])
        i = i + 1
    return is_a_valid_char


def is_a_valid_base(chain):
    return chain in base 


def is_bin(chain):
    return chain in is_bin_writing

def is_dec(chain):
    return chain in is_dec_writing

def is_hex(chain):
    return chain in is_hex_writing