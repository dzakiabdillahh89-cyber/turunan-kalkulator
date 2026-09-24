# Kalkulator Turunan Numerik - Project 2
# Target: TUB Physical Engineering
# Author: SMP Kelas 2 Garahan

def turunan(f, x, h=0.000001):
    """Hitung turunan pakai rumus f'(x) = (f(x+h)-f(x-h))/2h"""
    return (f(x+h) - f(x-h)) / (2*h)

# Contoh 1: f(x) = x^2 -> f'(x) = 2x
def f1(x):
    return x**2

# Contoh 2: f(x) = x^3 -> f'(x) = 3x^2
def f2(x):
    return x**3

# Contoh 3: f(x) = sin(x) -> f'(x) = cos(x)
import math
def f3(x):
    return math.sin(x)

print("=== KALKULATOR TURUNAN SMP KELAS 8 ===")
print(f"f(x)=x^2, f'(2) = {turunan(f1, 2)} (harusnya 4)")
print(f"f(x)=x^3, f'(2) = {turunan(f2, 2)} (harusnya 12)")
print(f"f(x)=sin(x), f'(0) = {turunan(f3, 0)} (harusnya 1 = cos(0))")
print("\nProject 2 done. Next: Integral")