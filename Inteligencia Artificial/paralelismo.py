import multiprocessing

def calculate_square(n):
    return n*n

if __name__ == '__main__':
    numbers = [1,2,3,4,5]
    with multiprocessing.Pool() as pool:
        result = pool.map(calculate_square, numbers)
        
    print(f"Result: {result}")