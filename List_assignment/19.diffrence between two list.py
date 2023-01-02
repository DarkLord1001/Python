#19. Write a Python program to get the difference between the two lists.
list_a=[1, 2, 3, 4, 5, 6, 'pink']
list_b=[1, 2, 3, 4, 5]
diff_list=list(set(list_a)-set(list_b))
print(diff_list)