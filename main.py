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
    (x) => 1 - 2 * x * Math.exp((-x)/ 2), (x) => (x - 2) * Math.exp((-x) / 2), 0
]
    