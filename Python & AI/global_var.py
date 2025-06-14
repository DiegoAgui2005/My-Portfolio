x = 5 #global variable
def modify_global():
    global x
    x +=3
    print(f"modified global variable: {x}")
    
modify_global()
print(x)