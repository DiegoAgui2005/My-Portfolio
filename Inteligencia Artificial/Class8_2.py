a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
c = a [:]
print(id(a))
print(id(b)) # It is the same memory address
print(id(c)) # It is a different memory address
a.append(6)
print((a))
print((b)) # It is the same memory address
print((c)) # It is a different memory address