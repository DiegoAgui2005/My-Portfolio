def add(a,b,c):
    return a + b + c

values = (1,2,3)
print(add(*values))

def show_info(name,age):
    print(f"Name:{name}, Age:{age}")
    
data = {"name":"Diego", "age":29}
show_info(**data)