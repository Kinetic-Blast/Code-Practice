def hex_string_to_RGB(hex_s): 
    return {'r': int(hex_s[1:3],16), 'g': int(hex_s[3:5],16), 'b': int(hex_s[5:7],16)}
