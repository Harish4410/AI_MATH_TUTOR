from sympy import symbols, Eq, solve, sympify
import re

def clean_equation(eq):

    eq = eq.replace("^","**")

    eq = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', eq)

    return eq

def solve_equation(eq_string):

    x = symbols('x')

    eq_string = clean_equation(eq_string)

    left, right = eq_string.split("=")

    equation = Eq(sympify(left), sympify(right))

    solution = solve(equation, x)

    steps = [
        f"Original Equation: {eq_string}",
        "Rearranging equation",
        "Solving for x"
    ]

    return solution, steps