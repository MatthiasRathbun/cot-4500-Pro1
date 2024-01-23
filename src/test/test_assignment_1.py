import unittest
import sys
from pathlib import Path

# Add the parent directory to sys.path to import the main module
parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir)
from main.assignment_1 import approximate_root_two, bisection_method, fixed_point_iteration, newton_method

def test_functions():
    print("Testing approximate_root_two:")
    print(approximate_root_two())

    print("\nTesting bisection_method with f(x) = x^2 - 2:")
    root = bisection_method(lambda x: x**2 - 2, 1, 2, 1e-5, 100)
    print(root)

    print("\nTesting fixed_point_iteration with g(x) = (1/2) * ((x+2)/x)):")
    fixed_point_result, message = fixed_point_iteration(lambda x: 0.5 * (x + 2 / x), 1.0, 1e-5, 25)
    print(fixed_point_result, message)

    print("\nTesting newton_method with f(x) = x^2 - 2:")
    newton_result, message = newton_method(lambda x: x**2 - 2, lambda x: 2*x, 1.0, 1e-5, 20)
    print(newton_result, message)

if __name__ == '__main__':
    test_functions()