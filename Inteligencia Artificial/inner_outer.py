x = "global" #global variable

#external function
def outer_function():
    x = "enclosing" #global variable
    
    #inner function
    def inner_function():
        x = "local" #local variable
        print(x)
        
    inner_function()
    print(x)
    
outer_function()
print(x)