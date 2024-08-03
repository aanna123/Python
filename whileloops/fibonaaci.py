numbers=[1,1]
n=5
i=2
while i<=n:
  new1=numbers[i-1]
  new2=numbers[i-2]
  numbers.append(new1+new2)
  i+=1
x=0
print("the fibonacci series is: ",end=" ")
while x < len(numbers):
  print(numbers[x],end=" ")
  x+=1
  
  
  
