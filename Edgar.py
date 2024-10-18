from math import*


def dec_to_hex (init_number):
    hex_number = ""
    hex_chars = "0123456789ABCDEF"

    while init_number > 0:
        point_hex_char = init_number % 16
        hex_number = hex_chars[point_hex_char] + hex_number
        init_number = init_number // 16
    return hex_number

print (dec_to_hex(91))


