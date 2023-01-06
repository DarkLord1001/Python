temp=input("Enter string : ")
a=temp
count={}
for i in temp.split(" "):
  if(i[0] not in count.keys()):
    count.update({i[0]:i})
  else:
    count.update({i[0]:[count[i[0]],i]})
print(count)