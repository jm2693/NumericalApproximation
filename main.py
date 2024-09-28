import math

# this is my implemented bisection method 
def bisectionMethod(f, a, b, epsilon=10e-6, max_iterations=100, result=None):
    if result is None:
        result = []
    if max_iterations == 0 or f(a) * f(b) >= 0:
        return result
    
    c = (a + b) / 2
    fc = f(c)
    
    result.append((len(result) + 1, a, b, c, fc))
    if abs(fc) < epsilon:
        return result
    
    if f(a) * fc < 0:
        return bisectionMethod(f, a, c, epsilon, max_iterations - 1)
    elif fc * f(b) < 0:
        return bisectionMethod(f, c, b, epsilon,  max_iterations - 1)
    
# this is my implemented Newton's method
def newtonMethod(f, df, x0, epsilon=10e-6, max_iterations=100, result=None):
    if result is None:
        result = []
    if max_iterations == 0:
        return result
    
    fx0 = f(x0)
    dfx0 = df(x0)

    result.append((len(result) + 1, x0, fx0))
    if abs(fx0) < epsilon:
        return result
    
    # return what we have if derivative becomes 0
    if dfx0 == 0:
        return result
    x1 = x0 - fx0 / dfx0
    return newtonMethod(f, df, x1, epsilon, max_iterations - 1, result)

# def newtonMethod(f, df, x0, epsilon=1e-6, max_iterations=100, result=None):
#     if result is None:
#         result = []
#     if max_iterations == 0:
#         return result
#     fx0 = f(x0)
#     dfx0 = df(x0)
#     result.append((len(result) + 1, x0, fx0))
#     if abs(fx0) < epsilon:
#         return result
#     if dfx0 == 0:
#         return result  # Avoid division by zero
#     x1 = x0 - fx0 / dfx0
#     return newtonMethod(f, df, x1, epsilon, max_iterations - 1, result)
    
# this is my implmented secant method
def secantMethod(f, x0, x1, epsilon=10e-6, max_iterations=100, result=None):
    if max_iterations == 0:
        return None
    
    if result == None:
        result = []
        
    x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
    fx2 = f(x2)
    
    result.append((len(result) + 1, x0, x1, x2, fx2))
    if fx2 < epsilon:
        return result
    
    return secantMethod(f, x1, x2, epsilon, max_iterations - 1, result)
    
given_functions = [
    (lambda x: 1 - 2 * x * math.exp((-x)/ 2), lambda x: (x - 2) * math.exp((-x) / 2), 0, 0.75),
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

def print_table(f, x0, df=None, x1=None, method_name="newton"):
    list_of_results = []
    if method_name == "bisection":
        print(f"{'Iteration':^10}{'a':^10}{'b':^10}{'c':^10}{'f(c)':^10}")
        list_of_results = bisectionMethod(f, x0, x1)
        for i, a, b, c, fc in list_of_results:
            print(f"{i:^10}{a:^10}{b:^10}{c:^10}{fc:^10}")
            
    elif method_name == "secant":
        print(f"{'Iteration':^10}{'x0':^10}{'x1':^10}{'x2':^10}{'f(x2)':^10}")
        list_of_results = secantMethod(f, x0, x1)
        for i, x0, x1, x2, fx2 in list_of_results:
            print(f"{i:^10}{x0:^10}{x1:^10}{x2:^10}{fx2:^10}")
        
    elif method_name == "newton":
        print(f"{'Iteration':^10}{'x':^15}{'f(x1)':^15}")
        list_of_results = newtonMethod(f, df, x0)
        for i, x, fx1 in list_of_results:
            print(f"{i:^15}{x:<15.7f}{fx1:<15.7f}")
        
print_table(given_functions[0][0], given_functions[0][2], given_functions[0][1])