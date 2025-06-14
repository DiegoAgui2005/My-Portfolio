class Counter:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count
    
Counter.increment()
Counter.increment()
print(Counter.count)  # Output: 2