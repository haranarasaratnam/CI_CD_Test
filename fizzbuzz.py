def fizzbuzz(n):
    """
    FizzBuzz function that returns 'Fizz' for multiples of 3,
    'Buzz' for multiples of 5, 'FizzBuzz' for multiples of both 3 and 5,
    and the number itself for all other cases.

    Parameters:
    - n (int): The number to check.

    Returns:
    - str: 'Fizz' if n is a multiple of 3, 'Buzz' if n is a multiple of 5,
      'FizzBuzz' if n is a multiple of both 3 and 5, otherwise the number itself.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# Pytest code to test the fizzbuzz function
import pytest

def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(30) == "FizzBuzz"
    #assert fizzbuzz(7) == "7"

# Run the pytest
if __name__ == "__main__":
    pytest.main([__file__])
