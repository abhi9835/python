a = 56 #global variable

def function_1():
    global a
    a = 5  #local variable
    print(a)

function_1()
print(a)