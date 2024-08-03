n=int(input("enter a number:"))
print("the binary number of {}: ".format(n),end=" ")
def dec(n):
  sum=[]
  while n != 0:
    digits=n%2
    sum.append(digits)
    n=n//2
    if n==0:
      i=len(sum)-1
      while i>=0:
        print(sum[i],end="")
        i-=1
  return sum


dec(n)

