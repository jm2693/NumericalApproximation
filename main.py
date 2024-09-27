import math

# this is my implemented bisection method 
def bisectionMethod(f, a, b, epsilon=1e-6, max_iterations=100):
    if max_iterations == 0 or f(a) * f(b) >= 0:
        return None
    
    c = (a + b) / 2
    
    if abs(f(c)) < epsilon:
        return c
    
    if f(a) * f(c) < 0:
        return bisectionMethod(f, a, c, epsilon, max_iterations - 1)
    elif f(c) * f(b) < 0:
        return bisectionMethod(f, c, b, epsilon,  max_iterations - 1)
    
def newtonMethod(f, df, x0, epsilon=1e-6, max_iterations=100):
    if max_iterations == 0:
        return None
    
    x0 = x0 - f(x0) / df(x0)
    
    if f(x0) < epsilon:
        return x0
    
    newtonMethod(f, df, x0, epsilon, max_iterations-1)
    
def secantMethod(f, x0, x1, epsilon=1e-6, max_iterations=100):
    if max_iterations == 0:
        return None
    
    x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
    
    if f(x2) < epsilon:
        return x2
    
given_functions = [
    (lambda x: 1 - 2 * x * math.exp((-x)/ 2), lambda x: (x - 2) * math.exp((-x) / 2), 0),
    (lambda x: 5 - x ** (-1), lambda x: x ** -2, 0.25),
    (lambda x: (x ** 3) - (2 * x) - 5, lambda x: (3 * x ** 2) - 2, 2),
    (lambda x: math.exp(x) - 2, lambda x: math.exp(x), 1),
    (lambda x: x - math.exp(-x), lambda x: 1 + math.exp(-x), 1),
    (lambda x: (x ** 6) - x - 1, lambda x: (6 * x ** 5) - 1, 1),
    (lambda x: x ** 2 - math.sin(x), lambda x: 2 * x - math.cos(x), 0.5),
    (lambda x: x ** 3 - 2, lambda x: 3 * x ** 2, 1),
    (lambda x: x + math.tan(x), lambda x: 1 + (math.sec(x)) ** 2, 3),
    (lambda x: 2 - (x ** (-1) * math.log(x)), lambda x: (math.log(x) - 1) / x ** 2, (1 / 3)),
]
    