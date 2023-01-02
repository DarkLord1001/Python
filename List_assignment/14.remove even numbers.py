#14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
list = [1, 2, 3, 4, 5]
list1=[x for x in list if x%2 != 0]
print(list1)