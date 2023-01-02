#Write a Python program to remove duplicates from a list.
my_list=[11, 22, 33, 44, 44, 55, 11, 32, 33, 44, 44, 55, 11, 11]
list = list(set(my_list))
print(list)