#16. Write a Python program to generate and print a list of first and last 5 elements where the values
# are square of numbers between 1 and 30 (both included).
my_list=[x**2 for x in range(1,31)]
print(my_list[:5],my_list[-5:])
