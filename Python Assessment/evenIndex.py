list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
list1 = [1, 1]

def is_on_even_position(list_param, value):
    if (list_param.index(value) % 2) == 0:
        return True
    else:
        return False

is_on_even_position(list, 6)
is_on_even_position(list, 3)
is_on_even_position(list1, 1)
