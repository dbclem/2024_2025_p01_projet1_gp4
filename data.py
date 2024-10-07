ask_for_init_number_text = "Entrez le numbre que vous voulez transformer : "
ask_again_for_init_number_text = "Ce n'est pas un nombre ! " + ask_for_init_number_text


ask_for_init_base_text = "Entrez la base que vous voulez utiliser : "
ask_again_for_init_base_text = "Ce n'est pas une base connu, vous devez rentrer du binaire, du decimale, ou de l'hexadecimal. \n" + ask_for_init_base_text

ask_for_target_base_text = "Entrez la base qeu vous voulez viser : "
ask_again_for_target_base_text = "Ce n'est pas une base connu, vous devez rentrer du binaire, du decimale, ou de l'hexadecimal. \n" + ask_for_target_base_text


bin_number_valid_chars = ["0", "1"]
dec_number_valid_chars = bin_number_valid_chars\
                        + ["2", "3", "4", "5", "6", "7", "8", "9"]
hex_number_valid_chars = dec_number_valid_chars\
                        + ["A", "B", "C", "D", "E", "F"]\
                        + ["a", "b", "c", "d", "e", "f"]


is_bin_writing = ["b", "bin", "binaire", "2"]
is_dec_writing = ["d", "dec", "decimal", "10"]
is_hex_writing = ["h", "hex", "hexadecimal", "16"]
base =  is_bin_writing\
        + is_dec_writing\
        + is_hex_writing
