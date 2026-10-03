def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    new_coefficient = c * n
    new_exponent = n - 1

    derivative = new_coefficient * (x ** new_exponent)

    return derivative