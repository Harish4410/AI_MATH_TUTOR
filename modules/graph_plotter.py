import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def plot_equation(eq):

    x = sp.symbols('x')

    left, right = eq.split("=")

    expr = sp.sympify(left) - sp.sympify(right)

    f = sp.lambdify(x, expr, "numpy")

    xs = np.linspace(-10,10,400)
    ys = f(xs)

    fig, ax = plt.subplots()

    ax.plot(xs, ys)

    ax.axhline(0)
    ax.axvline(0)

    ax.set_title("Equation Graph")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    return fig