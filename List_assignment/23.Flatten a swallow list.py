#23. Write a Python program to flatten a shallow list.
my_list = [[1, 2], [3, 4], [5]]
from itertools import chain

list =list(chain(*my_list))
print(list)