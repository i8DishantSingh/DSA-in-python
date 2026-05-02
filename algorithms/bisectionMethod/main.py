def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    # Handle negative input
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    # Handle exact cases
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    # Define initial interval
    low = 0
    high = max(1, number)  # ensures correct interval for numbers < 1

    # Perform iterations
    for i in range(max_iterations):
        mid = (low + high) / 2
        square = mid * mid

        # Check if within tolerance
        if abs(high - low) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid

        # Narrow down interval
        if square < number:
            low = mid
        else:
            high = mid

    # If not converged
    print(f"Failed to converge within {max_iterations} iterations.")
    return None
