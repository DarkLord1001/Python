#10.
#Appearing in a String Using a Dictionary
temp=input("Enter string : ")
count={}
for i in temp.split(" "):
  count.update({i:temp.count(i)})
print(count)