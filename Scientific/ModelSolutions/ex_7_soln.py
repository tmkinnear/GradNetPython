# Model solution for exercise 7 of the "Introduction to scientific Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd

def newton_raphson(alpha, n):
    x_high = alpha if alpha > 1 else 1
    x = x_high / 2
    for i in range(n):
        x -= (x**2 - alpha) / (2 * x)
    return x


for i in range(15):
    root = newton_raphson(9, i)
    print(i, root, abs(root - 3))
