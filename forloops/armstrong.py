for num in range(1,1000000):
  sum=0
  temp=num
  numofdigits=len(str(temp))
  while temp>0:
    digits=temp%10
    sum=sum+digits**numofdigits
    temp=temp//10
  if num==sum:
    print(sum)
