def outer_function():
    x = "enclosing" #global variable
    def inner_function():
        nonlocal x  # accessing enclosing scope
        x = "modified value" #global variable
        print(f"The value of inner is {x}")
    inner_function() #global
    print(f"The value of outer is {x}")
outer_function() #global