#26. Write a python program to check whether two lists are circularly identical.
list_a = [1, 2, 3, 4, 5]
list_b = [5, 1, 2, 3, 4]
def circularly_identical(list_a, list_b):
    if len(list_a) != len(list_b):
        return print('not circularly identical')
    double_a = list_a * 2   # double_a = list_a + list_a
    string_b = map(str, list_b)
    string_double_a = map(str, double_a)
    if ' '.join(string_b) in ' '.join(string_double_a):
        return print('circularly identical')
    else:
        return print('not circularly identical')

circularly_identical(list_a, list_b)