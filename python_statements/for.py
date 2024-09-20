#Example for lists and for loop
mylist = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0

for num in mylist:
    list_sum = list_sum + num
print(f"The list sum is {list_sum}")

#Example for string:
for element in 'Hello World':
    print(element)

#Example for tuple
tup = (1,2,3)

for item in tup:
    print(item)

#Example for tuple unpacking:
mylist1=[(1,2),(3,4),(5,6),(7,8)]
for a,b in mylist1:
    print(a)

#Example for tuple unpacking:
mylist2=[(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in mylist2:
    print(a)
    print(b)

#Example for iteration through a dictionary
d = {'k1':1,'k2':2,'k3':3}

for a,b in d.items():
    print(a)
    print(b)