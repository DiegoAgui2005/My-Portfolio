class Multiplierfactory:
    
    def __new__(cls, factor: int):
        print(f"MultiplierFactory.__new__ called with factor {factor}")
        return super(Multiplierfactory, cls).__new__(cls)
    
    def __init__(self, factor: int):
        print(f"MultiplierFactory created with factor {factor}")
        self.factor = factor
        
    
    
    def __call__(self, number: int) -> int:
        return number * self.factor
    
multiplier = Multiplierfactory(5)
result = multiplier(10)
print(result) # Printing the result of the function