#6. Write a Python program to get a list, sorted in increasing order by the last element in each Tuple from a
# given list of non-empty Tuples. Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list.sort(key=lambda x: x[1])
print(list)