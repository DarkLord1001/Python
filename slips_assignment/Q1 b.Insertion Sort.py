def insertion_sort(my_list):

    for i in range(1,len(my_list)):
        loc=i
        for j in range(i-1,-1,-1):
            if my_list[loc]<my_list[j]:
                temp=my_list[loc]
                my_list[loc]=my_list[j]
                my_list[j]=temp
                loc=j


x=[14,46,43,27,57,41,45,21,70,15]
insertion_sort(x)
print(x)
y=[5,1,4,2,8]
insertion_sort(y)
print(y)