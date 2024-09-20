x = 4

while x < 5:
    print(f"The current value of x is {x}")
    x += 1
else:
    print("X is not less than 5")

#break, continue, pass
#break: breaks out of the current closest encoling loop.
#continue: goes to the top of the closest encoling loop.
#pass: does nothing at all.

#Example of pass
y = [1,2,3]

for item in y:
    pass
print('End of my script')

#Example of continue
mystring = 'Sammy'

for letter in mystring:
    if letter == 'm':
        continue
    print(letter)

#Example of break
z = 0

while z < 5:
    if z == 2:
        break    
    print(z)
    z += 1
