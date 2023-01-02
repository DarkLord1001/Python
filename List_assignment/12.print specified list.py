#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# solution 1
new_list=[]
for index,value in enumerate(my_list):
    if index not in [0,4,5]:
        new_list.append(value)
print(new_list)