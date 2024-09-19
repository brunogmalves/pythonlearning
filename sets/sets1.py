#It is also possible to use a kind of element which is not possible to "double" elements.
#It is called set.
#Lets see an example:

#creating a set
myset = set()
print(type(myset))

#to add an element to the set, it is done using add
myset.add(1)
print(myset)

#adding another elements
myset.add(2)
myset.add(3)
print(myset)

#trying to add something that is already in:
myset.add(2)
print(myset)

#example of usage
mylist = [1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5]
listset = set(mylist)
print(listset)

mylist.sort()