#18. Write a Python program to generate all permutations of a list in Python.
import itertools

my_list = [1, 2, 3, 4, 5]
print(list(itertools.permutations(my_list)))