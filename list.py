# list

x = [i for i in range(5)]
print(x)
print(len(x))

my_list = [ 10,5,6,"face","eye"]
my_list.append(7)
my_list.append('nose')
print(my_list)

for i in range (10,15):
  my_list.append(i)
  print(my_list)  


my_list.extend([2,4,5,9])
print(my_list)
my_list.append([4,8,9])
print(my_list)

my_list.insert(0,44)
my_list.insert(4,'hand')
print(my_list)

my_list.remove('nose')
print(my_list)

my_list.pop(0)
print(my_list)

print(my_list[0:3])


print(my_list[5:-3])
my_list.reverse()
print(my_list)

my_newlist = [i for i in range(11)]
print(min(my_newlist))
print(max(my_newlist))

my_list.count(0)

print(my_newlist+my_list+x)

print(my_list.index(9))

mylist = [(1,2,3),(4,5,6),(7,8,9)]
print(mylist)
