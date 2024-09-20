#The operator range() can generate a number sequence which we can go through 
#For example:
my_list = [1,2,3]
for num in range(0,11,2):
    print(num)
#Notice: The last number which the range goes to is equal i-1.
#Another interesting fact is that the range operator is a generator.
#So, if we want to store the sequence, we have to use mylist = list(range(from,to,step))
#It saves memory!!!

#_________________________________________________________#
#Another nice operator is enumerate. Lets see an example without it:
index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count += 1

#In order to do it easily and also "map" the string or list, it is possible to use enumerate:
mystring = 'abcde'

for index,letter in enumerate(mystring):
    print(letter)

#_________________________________________________________#
#Now, it is important to know about zip operator.
#It zips something on the memory or pair up items.
#For example:
mylist1 = [1,2,3]
mylist2 = ['a','b','c']

print(zip(mylist1,mylist2))

#We can group it on code using:
for a,b in zip(mylist1,mylist2):
    print(b)
#Zip will ignore different sized objects.

#_________________________________________________________#
#in is used to quickly verify if something is present on another place. For example:
print('mkey' in {'mkey':345})

#min(list) and max(list) can find the minimum and the maximum number on a list
#also, there is the random library, on which we can import some function.
from random import shuffle

ordered_list = [0,1,2,3,4,5,6,7,8,9,10]
shuffle(ordered_list)
print(ordered_list)

from random import randint
print(randint(0,100))

#input can ask something for the user. Example,

name = input('Hey! What is your name? ')
print(f"Hello, {name}!")







