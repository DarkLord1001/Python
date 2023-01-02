#10. Write a Python program to find the list of words that are longer than n from a given list of words.
list1=['cat','Dog','Modern','shivajinagar']
n=int(input("Enter Limit of word::"))
long_word=[]
for i in list1:
    if len(i) > n:
        long_word.append(i)
print(long_word)