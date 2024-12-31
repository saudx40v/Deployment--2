def sum_even_numbers(numbers):
    """
    Function to calculate the sum of even numbers in a list.
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    return even_sum

# Example usage
if __name__ == "__main__":
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("The sum of even numbers is:", sum_even_numbers(numbers_list))
