#A tuple is similar to a list, but it cannot be modified.
#It means: Immutability

#Defining a tuple:
t = (1,2,3,1)

#Verifying the type and lenght of t:
print(type(t))
print(len(t))
print(t)

#It is also possible to verify the last value of a tuple using index -1.
print(t[-1])

#You can count the number of episodes that something appears on a tuple, just using:
print(t.count(1))

#To see the very first time some value appears, it is possible to use
print(t.index(2))

#Checking the immutability:
#t[0] = 'NEW'
#t[0] = 2

#SO: Why use tuples?
#It is more used on advanced programming, to avoid accidental changes.