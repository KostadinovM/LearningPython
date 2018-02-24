#Functions

#Defining a function
def example():
    #here goes the function block
    print('basic function')
    z = 3+9
    print(z)

#Call a function
example()

#Function with parameters
def simple_addition(num1, num2):
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)

simple_addition(5,3)

def simple(num1, num2):
    pass #makes it just do something so it doesnt throw an error

#Function with default parameters
def simple(num1, num2=5):
    print(num1, num2)

simple(2)

def basic_window(width, height, font='TNR',
                 bgc='w', scrollbar=True):
    print(width, height, font, bgc, scrollbar)

basic_window(500,350)
basic_window(500,350, 'w')
basic_window(500,350, bgc='w')  #refering to a specific parameter

