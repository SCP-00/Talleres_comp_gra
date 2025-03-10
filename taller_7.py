import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def exp_taylor(x, n_terms=20):
    result = 0
    for n in range(n_terms):
        result += x**n / factorial(n)
    return result

def sin_taylor(x, n_terms=20):
    result = 0
    for n in range(n_terms):
        result += ((-1)**n) * x**(2*n+1) / factorial(2*n+1)
    return result

def cos_taylor(x, n_terms=20):
    result = 0
    for n in range(n_terms):
        result += ((-1)**n) * x**(2*n) / factorial(2*n)
    return result

def tan_taylor(x, n_terms=20):
    return sin_taylor(x, n_terms) / cos_taylor(x, n_terms)

def ln_taylor(x, n_terms=20):
    if x <= 0:
        raise ValueError("ln(x) is undefined for x <= 0")
    y = (x - 1) / (x + 1)
    result = 0
    for n in range(n_terms):
        result += (1 / (2*n + 1)) * y**(2*n+1)
    return 2 * result

def plot_taylor_series(plot_all=True, individual_plots=False):
    x = np.linspace(-2, 2, 400)
    x_ln = np.linspace(0.1, 2, 400)

    vec_exp = np.vectorize(exp_taylor)
    vec_sin = np.vectorize(sin_taylor)
    vec_cos = np.vectorize(cos_taylor)
    vec_tan = np.vectorize(tan_taylor)
    vec_ln  = np.vectorize(ln_taylor)

    y_exp = vec_exp(x)
    y_sin = vec_sin(x)
    y_cos = vec_cos(x)
    y_tan = vec_tan(x)
    y_ln  = vec_ln(x_ln)

    if plot_all:
        plt.figure(figsize=(10,6))
        plt.plot(x, y_exp, label="exp(x)")
        plt.plot(x, y_sin, label="sin(x)")
        plt.plot(x, y_cos, label="cos(x)")
        plt.plot(x, y_tan, label="tan(x)")
        plt.plot(x_ln, y_ln, label="ln(x)")

        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Taylor Series Approximations of exp, sin, cos, tan and ln")
        plt.legend()
        plt.grid(True)
        plt.show()

    if individual_plots:
        # Plot each function individually
        plt.figure(figsize=(8, 6))
        plt.plot(x, y_exp, label="exp(x)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Taylor Series Approximation of exp(x)")
        plt.legend()
        plt.grid(True)
        plt.show()

        plt.figure(figsize=(8, 6))
        plt.plot(x, y_sin, label="sin(x)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Taylor Series Approximation of sin(x)")
        plt.legend()
        plt.grid(True)
        plt.show()

        plt.figure(figsize=(8, 6))
        plt.plot(x, y_cos, label="cos(x)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Taylor Series Approximation of cos(x)")
        plt.legend()
        plt.grid(True)
        plt.show()

        plt.figure(figsize=(8, 6))
        plt.plot(x, y_tan, label="tan(x)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Taylor Series Approximation of tan(x)")
        plt.legend()
        plt.grid(True)
        plt.show()

        plt.figure(figsize=(8, 6))
        plt.plot(x_ln, y_ln, label="ln(x)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Taylor Series Approximation of ln(x)")
        plt.legend()
        plt.grid(True)
        plt.show()

def menu():
    while True:
        print("\nTaylor Series Plot Menu:")
        print("1. Plot all functions in one graph")
        print("2. Plot each function individually")
        print("3. Plot none")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            plot_taylor_series(plot_all=True, individual_plots=False)
        elif choice == '2':
             plot_taylor_series(plot_all=False, individual_plots=True)
        elif choice == '3':
            plot_taylor_series(plot_all=False, individual_plots=False)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    menu()
