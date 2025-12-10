i = 0


def binary_to_decimal(bin_value):
    i = 0
    a = len(bin_value)
    dec_list = []
    while i < len(bin_value):
        inter_value = int(bin_value[a-1]) * 2**i
        dec_list.insert(0, inter_value)
        i += 1
        a -= 1
    i = 0
    final_value = 0
    while i < len(bin_value):
        final_value = final_value + dec_list[i]
        i += 1
    return final_value


def binary_to_octal(bin_value):
    g = len(bin_value)
    if (g % 3) != 0:
        i = 0
        str_bin_value = ''
        if g == 4 or g == 7 or g == 1 or g == 10 or g == 13:
            bin_value = list(bin_value)
            bin_value.insert(0, '00')
            while i < len(bin_value):
                str_bin_value = str_bin_value + bin_value[i]
                i += 1
            bin_value = str_bin_value
        if g == 2 or g == 5 or g == 8 or g == 11 or g == 14:
            bin_value = list(bin_value)
            bin_value.insert(0, '0')
            while i < len(bin_value):
                str_bin_value = str_bin_value + bin_value[i]
                i += 1
            bin_value = str_bin_value
    length_of_value = len(bin_value)
    i = 0
    a = length_of_value
    fin_list = []
    while i < length_of_value:
        part = bin_value[(a-3):a]
        k = 0
        x = len(part)
        oct_list = []
        while k < len(part):
            inter_value = str(int(part[x-1]) * (2 ** k))
            oct_list.insert(0, inter_value)
            k += 1
            x -= 1
        inter_inter_value = ''
        k = 0
        while k < len(oct_list):
            inter_inter_value = inter_inter_value + oct_list[k]
            k += 1
        k = 0
        while k < len(inter_inter_value):
            inter_inter_value = list(inter_inter_value)
            inter_inter_value[k] = int(inter_inter_value[k])
            k += 1
        inter_inter_value = sum(list(inter_inter_value))
        fin_list.insert(0, inter_inter_value)
        i += 3
        a -= 3
    i = 0
    final_value = ''
    while i < len(fin_list):
        fin_list[i] = str(fin_list[i])
        final_value = final_value + fin_list[i]
        i +=1
    return final_value


def binary_to_hexadecimal(bin_value):
    g = len(bin_value)
    if (g % 4) != 0:
        i = 0
        str_bin_value = ''
        if g == 2 or g == 6 or g == 10 or g == 14 or g == 18:
            bin_value = list(bin_value)
            bin_value.insert(0, '00')
            while i < len(bin_value):
                str_bin_value = str_bin_value + bin_value[i]
                i += 1
            bin_value = str_bin_value
        if g == 3 or g == 7 or g == 11 or g == 15 or g == 19:
            bin_value = list(bin_value)
            bin_value.insert(0, '0')
            while i < len(bin_value):
                str_bin_value = str_bin_value + bin_value[i]
                i += 1
            bin_value = str_bin_value
    length_of_value = len(bin_value)
    i = 0
    a = length_of_value
    fin_list = []
    while i < length_of_value:
        part = bin_value[(a - 4):a]
        k = 0
        x = len(part)
        oct_list = []
        while k < len(part):
            inter_value = str(int(part[x - 1]) * (2 ** k))
            oct_list.insert(0, inter_value)
            k += 1
            x -= 1
        inter_inter_value = ''
        k = 0
        while k < len(oct_list):
            inter_inter_value = inter_inter_value + oct_list[k]
            k += 1
        k = 0
        while k < len(inter_inter_value):
            inter_inter_value = list(inter_inter_value)
            inter_inter_value[k] = int(inter_inter_value[k])
            k += 1
        inter_inter_value = sum(list(inter_inter_value))
        if inter_inter_value >= 10:
            if inter_inter_value == 10:
                inter_inter_value = 'A'
            elif inter_inter_value == 11:
                inter_inter_value = 'B'
            elif inter_inter_value == 12:
                inter_inter_value = 'C'
            elif inter_inter_value == 13:
                inter_inter_value = 'D'
            elif inter_inter_value == 14:
                inter_inter_value = 'E'
            else:
                inter_inter_value = 'F'
        fin_list.insert(0, inter_inter_value)
        i += 4
        a -= 4
    i = 0
    final_value = ''
    while i < len(fin_list):
        fin_list[i] = str(fin_list[i])
        final_value = final_value + fin_list[i]
        i += 1
    return final_value


def decimal_to_binary(dec_number):
    i = 0
    dec_list = []
    dec_str = ''
    g = int(dec_number) % 2
    while True:
        g = int(dec_number) % 2
        if g == 0:
            dec_number = int(dec_number) / 2
            dec_list.insert(0, '0')
            continue
        elif int(dec_number) == 1:
            dec_list.insert(0, '1')
            break
        else:
            dec_number = (int(dec_number) - 1) / 2
            dec_list.insert(0, '1')
            continue
    while i < len(dec_list):
        dec_str = dec_str + dec_list[i]
        i += 1
    final_value = dec_str
    return final_value


def decimal_to_octal(dec_number):
    inter_value = decimal_to_binary(dec_number)
    final_value = binary_to_octal(inter_value)
    return final_value


def decimal_to_hexadecimal(dec_number):
    inter_value = decimal_to_binary(dec_number)
    final_value = binary_to_hexadecimal(inter_value)
    return final_value


def octal_to_decimal(oct_value):
    i = 0
    a = len(oct_value)
    dec_list = []
    while i < len(oct_value):
        inter_value = int(oct_value[a - 1]) * 8 ** i
        dec_list.insert(0, inter_value)
        i += 1
        a -= 1
    i = 0
    final_value = 0
    while i < len(oct_value):
        final_value = final_value + dec_list[i]
        i += 1
    return final_value


def hexadecimal_to_decimal(hex_value):
    i = 0
    a = len(hex_value)
    dec_list = []
    while i < len(hex_value):
        if hex_value[a-1] in ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']:
            hex_value = list(hex_value)
            k = 0
            hex_inter_str = ''
            if hex_value[a - 1] == 'A' or hex_value[a - 1] == 'a':
                hex_value[a - 1] = '10'
                hex_inter_str = hex_value[a-1]
                hex_value[a - 1] = hex_inter_str
            elif hex_value[a - 1] == 'B' or hex_value[a - 1] == 'b':
                hex_value[a - 1] = '11'
                hex_inter_str = hex_value[a - 1]
                hex_value[a-1] = hex_inter_str
            elif hex_value[a - 1] == 'C' or hex_value[a - 1] == 'c':
                hex_value[a - 1] = '12'
                hex_inter_str = hex_value[a - 1]
                hex_value[a-1] = hex_inter_str
            elif hex_value[a - 1] == 'D' or hex_value[a - 1] == 'd':
                hex_value[a - 1] = '13'
                hex_inter_str = hex_value[a - 1]
                hex_value[a-1] = hex_inter_str
            elif hex_value[a - 1] == 'E' or hex_value[a - 1] == 'e':
                hex_value[a - 1] = '14'
                hex_inter_str = hex_value[a - 1]
                hex_value[a-1] = hex_inter_str
            elif hex_value[a - 1] == 'F' or hex_value[a - 1] == 'f':
                hex_value[a - 1] = '15'
                hex_inter_str = hex_value[a - 1]
                hex_value[a-1] = hex_inter_str
        inter_value = int(hex_value[a - 1]) * 16 ** i
        dec_list.insert(0, inter_value)
        i += 1
        a -= 1
    i = 0
    final_value = 0
    while i < len(hex_value):
        final_value = final_value + dec_list[i]
        i += 1
    return final_value


def octal_to_binary(oct_value):
    inter_value = octal_to_decimal(oct_value)
    final_value = decimal_to_binary(inter_value)
    return final_value


def hexadecimal_to_binary(hex_value):
    inter_value = hexadecimal_to_decimal(hex_value)
    final_value = decimal_to_binary(inter_value)
    return final_value


def octal_to_hexadecimal(oct_value):
    inter_value = octal_to_decimal(oct_value)
    final_value = decimal_to_hexadecimal(inter_value)
    return final_value


def hexadecimal_to_octal(hex_value):
    inter_value = hexadecimal_to_decimal(hex_value)
    final_value = decimal_to_octal(inter_value)
    return final_value



print('''1. type bin_to_dec for binary to decimal
    2. type bin_to_oct for binary to octal
    3. type bin_to_hex for binary to hexadecimal
    4. type dec_to_bin for decimal to binary
    5. type dec_to_oct for decimal to octal
    6. type dec_to_hex for decimal to hexadecimal
    7. type oct_to_dec for octal to decimal
    8. type hex_to_dec for hexadecimal to decimal
    9. type oct_to_bin for octal to binary
    10. type hex_to_bin for hexadecimal to binary:
    11. type oct_to_hex for octal to hexadecimal
    12. type hex_to_oct for hexadecimal to octal''')
while True:
    user_req = input('What type of conversion do you need(type "quit" to quit): ')
    if user_req.upper() == 'BIN_TO_DEC':
        user_val = input('Input the binary value: ')
        if '2' in user_val or '3' in user_val or '4' in user_val or '5' in user_val or '6' in user_val or '7' in user_val or '8' in user_val or '9' in user_val:
            print('Please input an valid binary number!')
            continue
        result = binary_to_decimal(user_val)
        print(f'{user_val} to decimal value is: {result}')
    elif user_req.upper() == 'BIN_TO_OCT':
        user_val = input('Input the binary value: ')
        if '2' in user_val or '3' in user_val or '4' in user_val or '5' in user_val or '6' in user_val or '7' in user_val or '8' in user_val or '9' in user_val:
            print('Please input an valid binary number!')
            continue
        result = binary_to_octal(user_val)
        print(f'{user_val} to octal value is: {result}')
    elif user_req.upper() == 'BIN_TO_HEX':
        user_val = input('Input the binary value: ')
        if '2' in user_val or '3' in user_val or '4' in user_val or '5' in user_val or '6' in user_val or '7' in user_val or '8' in user_val or '9' in user_val:
            print('Please input an valid binary number!')
            continue
        result = binary_to_hexadecimal(user_val)
        print(f'{user_val} to hexadecimal value is: {result}')
    elif user_req.upper() == 'DEC_TO_BIN':
        user_val = input('Input the decimal value: ')
        result = decimal_to_binary(user_val)
        print(f'{user_val} to binary value is: {result}')
    elif user_req.upper() == 'DEC_TO_OCT':
        user_val = input('Input the decimal value: ')
        result = decimal_to_octal(user_val)
        print(f'{user_val} to octal value is: {result}')
    elif user_req.upper() == 'DEC_TO_HEX':
        user_val = input('Input the decimal value: ')
        result = decimal_to_hexadecimal(user_val)
        print(f'{user_val} to hexadecimal value is: {result}')
    elif user_req.upper() == 'OCT_TO_DEC':
        user_val = input('Input the octal value: ')
        if '8' in user_val or '9' in user_val:
            print('Please input an valid octal number!')
            continue
        result = octal_to_decimal(user_val)
        print(f'{user_val} to decimal value is: {result}')
    elif user_req.upper() == 'HEX_TO_DEC':
        user_val = input('Input the hexadecimal value: ')
        result = hexadecimal_to_decimal(user_val)
        print(f'{user_val} to decimal value is: {result}')
    elif user_req.upper() == 'OCT_TO_BIN':
        user_val = input('Input the octal value: ')
        if '8' in user_val or '9' in user_val:
            print('Please input an valid octal number!')
            continue
        result = octal_to_binary(user_val)
        print(f'{user_val} to binary value is: {result}')
    elif user_req.upper() == 'HEX_TO_BIN':
        user_val = input('Input the hexadecimal value: ')
        result = hexadecimal_to_binary(user_val)
        print(f'{user_val} to binary value is: {result}')
    elif user_req.upper() == 'OCT_TO_HEX':
        user_val = input('Input the octal value: ')
        if '8' in user_val or '9' in user_val:
            print('Please input an valid octal number!')
            continue
        result = octal_to_hexadecimal(user_val)
        print(f'{user_val} to hexadecimal value is: {result}')
    elif user_req.upper() == 'HEX_TO_OCT':
        user_val = input('Input the hexadecimal value: ')
        result = hexadecimal_to_octal(user_val)
        print(f'{user_val} to octal value is: {result}')
    elif user_req.upper() == 'QUIT':
        print('Bye! See you again!')
        break
    else:
        print('Please type a valid command!')






