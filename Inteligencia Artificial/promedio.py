def calculate_average(number):
    """
    Calculate the average of a list of number.
    Parameters:
    Numbers: List of numbers.
    A list can be string or float numbers
    
    Returns:Float: The average of the list of numbers
    """
    return sum(number) / len(number)

print(calculate_average([1,2,3,4,5]))