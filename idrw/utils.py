def int_list_to_hex(list_of_ints):
    if len(list_of_ints) == 1:
        ret_val = list_of_ints[0]
        return ret_val
    ret_value = list_of_ints[0] * 16 ** 2 + list_of_ints[1]
    ret_list = [ret_value]
    ret_list.extend(list_of_ints[2:])
    return int_list_to_hex(ret_list)