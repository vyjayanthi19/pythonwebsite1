a = 5 
def f():
    print ("Inside f():",a)
def g ():
    a =2 
    print("Inside g():",a)
def h ():
    global a 
    a=4 
    print("Inside h():",a) 

print("global :",a)
f()
print("global:",a)
g()
print("global:",a)
h ()
print("global :",a)