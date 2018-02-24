#Printing and Strings

#the \ is used as an escape character
#and basically makes sure to ignore the next char

#single quotes
print('This is an example of a print function.')
print('He said "Hi"')
print('We\'re going to the  scope')

#double quotes
print("He said \"Hi\" ") 
print("We're going to the store")

#adding two strings together
print('Hi' + 'There')   #won't leave a space between
print('Hi', 'There')    #will leave a space between

#strings and numbers
print('Hi', 5)
print('Hi' + str(5))    #print('Hi' + 5) will result in an error
print(int('8') + 5)     #print('8' + 5) will result in an error
print(float('8.5') + 5)

