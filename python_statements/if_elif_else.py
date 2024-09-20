#This lesson is focused on explain how to deal with flow control.
#It is important to notice that, many times, it is important to deal with flows on Python,
#specially if we have conditions.
#In order to deal with it, we use if, elif, and else statements.


#If is used to set the first condition and we just enter on it if the response is True.
#Else is the other route.
#Ex:
hungry = False

if hungry:
    print("Feed me!")
else:
    print("I'm Ok!")

#Another example, using multiconditional:
loc = 'Bank'

if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store!')
else:
    print('I do not know much.')

#Identation is essential for this usage
name = 'Sammy'

if name == 'Frankie':
    print('Hello, Frankie!')
elif name == 'Sammy':
    print('Hello, Sammy!')
else:
    print('What is your name?')

#For loops
mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    #check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

