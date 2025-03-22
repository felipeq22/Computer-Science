def perform_calculation(value1: float, value2: float, operation: str) -> float:
    """
    Perform a mathematical operation on two values.

    Parameters:
        value1 (float): The first value.
        value2 (float): The second value.
        operation (str): The operation to perform. Can be 'add', 'subtract', 'divide', or 'multiply'.

    Returns:
        float: The result of the operation.

    Raises:
        ZeroDivisionError: If attempting to divide by zero.
    """
    if operation == 'add':
        result = value1 + value2
    elif operation == 'subtract':
        result = value1 - value2
    elif operation == 'divide':
        result = value1 / value2
    else:
        result = value1 * value2

    return result


def convert_to_float(value1: str, value2: str) -> tuple[float, float]:
    """
    Convert two strings to floating point numbers.

    Parameters:
        value1 (str): The first value to convert.
        value2 (str): The second value to convert.

    Returns:
        tuple[float, float]: A tuple containing the converted float values of value1 and value2.

    Raises:
        ValueError: If either value1 or value2 cannot be converted to a float.
    """

    float_value1 = float(value1)
    float_value2 = float(value2)

    return float_value1, float_value2