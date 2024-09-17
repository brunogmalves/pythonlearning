#creating a list
number = [1, 5, 542, 12.5, 142, 567.1, -144, 0]
print(f'The original list is {number}')

#it is possible to sort the list, just inserting the method bellow:
number.sort()
print(f'The sorted list is {number}')
#IMPORTANT: The list is autommatically sorted and you lose the original order.
#If you want to maintain it, you can save it before the sorting.

#Another interesting feature is the possibility of reversing the list, just
#using the method reverse.
number.reverse()
print(f'The sorted and reversed list is {number}')

#To remove an object inside of the list, the method pop is used. Eg:
number.pop(4)
print(f'The popped list is {number}')

#Dictionaries are an interesting stuff to use, due to its possibility of indexing
#something. For example:

my_first_dict = {'name':'Bruno','age':23,'height':1.82,'weight':75}
print(my_first_dict['name'])