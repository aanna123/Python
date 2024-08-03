num=int(input("enter the number: "))
list=[]
list.append(num)
i=0
while (list[i] != 1):
  list.append(num)
  if list[i]%2==0:
    list[i+1]=list[i]//2
  else:
    list[i+1]=(list[i]*3)+1
  i=i+1
print(list)
