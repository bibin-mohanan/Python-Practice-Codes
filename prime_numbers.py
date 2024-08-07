########## print prime numbers from 100 to 200

upp= 200
low=100
count=0

for x in range (low,upp):
  for y in range(2,x):
    if (x%y == 0):
      flag=1
      
      break
    else:
      flag=0
      
      
  if flag==0:
    print(x) 
    count=count+1

print(count) 