#%%
import sympy as sp

#%%
def generate_polynomial(data, n_symbols):
    # Convert data to polynomial coefficients
    x = sp.symbols('x')
    polynomial = sum([data[i] * x**i for i in range(len(data))])
    return polynomial, x

def encode(polynomial, x, n_symbols):
    # Generate encoded symbols by evaluating the polynomial at different points
    encoded_symbols = [polynomial.subs(x, i) for i in range(1, n_symbols + 1)]
    return encoded_symbols

def introduce_erasures(encoded_symbols, n_erasures):
    # Randomly introduce erasures (simulate data loss)
    import random
    erasures = random.sample(range(len(encoded_symbols)), n_erasures)
    for e in erasures:
        encoded_symbols[e] = None  # None represents a lost symbol
    return encoded_symbols, erasures

def decode(encoded_symbols, erasures, n, x):
    # Decode the polynomial using interpolation
    points = [(i, symbol) for i, symbol in enumerate(encoded_symbols, start=1) if symbol is not None]
    lagrange_poly = sp.interpolate(points, x)
    return [lagrange_poly.subs(x, i) for i in range(1, n + 1)]

#%%
# Parameters
k = 4  # number of data symbols
n = 7  # total symbols (data + parity)

# Original data
data = [1, 0, 3, 4]  # example data coefficients for polynomial
print("Original data:", data)

# Encode data
poly, x = generate_polynomial(data, n)
encoded = encode(poly, x, n)
print("Encoded symbols:", encoded)

# Introduce erasures
encoded_with_erasures, erasures = introduce_erasures(encoded, 3)
print("Encoded symbols with erasures:", encoded_with_erasures)

# Decode the original data
decoded = decode(encoded_with_erasures, erasures, k, x)
print("Decoded original data:", decoded)

# %%
