# -*- coding: utf-8 -*-

#**************************************************
#**** author: Razafimiandrisoa Noarison Léonce ****
#**************************************************

def replace(str_origin,str_to_insert,start_position,end_position):
    """
        str_origin: (string) texte origine qui va etre traité
        str_to_insert: (string) texte a inserer
        start_position: (integer) la position initial ou mettre le texe (str_to_insert)
        end_position: (integer) la position final ou mettre le texe (str_to_insert)
    """
    str_origin = str(str_origin)
    str_to_insert = str(str_to_insert)
    start_position = int(start_position)
    end_position = int(end_position)
    first = str_origin[:start_position]
    two = str_to_insert
    three = str_origin[end_position:]
    text_origin_copy = str(first) + str(two) + str(three)

    return text_origin_copy
