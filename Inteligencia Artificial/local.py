x = 100

def local_function():
    x = 10 # Local variable
    print(f"The value of the local variable is {x}")

def global_function():
    print("The value of the global variable is {x}")
    
print(x) # This will raise an error because x is a local variable