def linearsearch(arr,x):
   for i in range(len(arr)):
      if arr[i]==x:
         return i
   return -1
arr = ['t','u','t','o','r','i','a','l']
x = input("enter char::")
print("Character found at index "+str(linearsearch(arr,x)))