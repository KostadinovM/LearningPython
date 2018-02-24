#Global and Local Variables
x = 6

def example():
    z=5
    print(x)
    print(x+5)
    #x+=6 doesnt work cause its not global var

def example1():
    global x
    print(x)
    x+=5
    print(x)

#Instead of using global var
def example2():
    globx = x
    print(globx)
    globx+=5
    print(x)

    return globx

example()
x=example2()
