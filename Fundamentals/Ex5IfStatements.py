#If-Statements

#If statement
x=5
y=8
z=5;
a=3;

if x>y:
    print('x is greater than y')
    
if x<y:
    print('y is greater than x')

if z<y>x:
    print('y is greater than z and x')

if z<y>x>a:
    print('y is greater than z and x and x is greater than a')

if z <= x:
    print('z is less than or equal to x')

if z == x:  #z=x won't work
    print('z is equal to x')

if z!=x:
    print('z does not equal x')
    

#If-Else Statement
if x>y:
    print('x is greater than y')
if x<55:
    print('x is greater than 55')
else:
    print('x is not greater than y')

#If Elif Else Statement
if x>y:
    print('x is greater than y')
elif x<z:
    print('x is less than z')
elif 5>2:
    print('5 is greater than 2')
else:
    print('if and elif(s) never ran)
