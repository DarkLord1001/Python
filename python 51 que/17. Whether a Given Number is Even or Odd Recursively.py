#17.
def even_odd(n):
  if(n==1):
    return "Odd Number"
  elif(n==0):
    return "Even Number"
  else:
    return even_odd(n-2)

n=int(input("Enter number to find even or odd "))
print(even_odd(n))