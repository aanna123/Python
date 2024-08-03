num=int(input("enter a number to be reversed: "))
temp=num
numbers=[]
while temp>0:
  digits=temp%10
  numbers.append(digits)
  temp=temp//10
i=0
print("\n the reversed number of {} is : ".format(num),end=" ")
while i<len(numbers):
  print(numbers[i],end="")
  i+=1

'''num=list(input("numer: "))
for i in reversed(num):
  print(i,end="")'''

