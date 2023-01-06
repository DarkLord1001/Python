temp=input("Enter string : ")
coun=0
for i in ('a','e','i','o','u'):
  coun+=temp.count(i.lower())
print("Number of vowels is ",coun)