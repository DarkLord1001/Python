#5. Write a Python program to count the number of strings where the string length is 2 or more and the first
# and last character are same from a given list of strings.
list=['om','madam','sir','ffdugf']
cnt=0
for i in list:
    if len(i) > 2 :
        if i[0] == i[-1]:
            cnt=cnt+1
print(cnt)