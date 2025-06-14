def divide(a: int, b: int) -> float:
   # valid that both parameters are integers
   if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both parameters must be integers")
   # valid that the second parameter is not zero
   if b == 0:
        raise ValueError("The divisor must not be zero")
    
   return a/b

#Example of use
try:
    res = divide(10, 0) # DivisionError
    print(res)
except ValueError as e:
    print(f"Error: {e}")