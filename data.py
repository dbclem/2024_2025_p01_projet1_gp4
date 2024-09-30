ask_for_init_number_text = "Entrez le numbre que vous voulez transformer : "
ask_again_for_init_number_text = "un nombre svp : "


ask_for_init_base_text = "Entrez la base que vous voulez utiliser : "
ask_again_for_init_base_text = "La bonne base svp : "

ask_for_target_base_text = "Entrez la base qeu vous voulez viser : "
ask_again_for_target_base_text = "la bonne base svp : "


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
