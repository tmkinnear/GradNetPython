# Model solution for exercise 6 of the "Introduction to scientific Python workshop"
# Copyright T.M. Kinnear & Leon Schoonderwoerd


def find_root(alpha, n):
    x_high = alpha if alpha > 1 else 1  # This is a compact if-else statement. Can you decipher it?
    x_low = 0
    x_mid = (x_low + x_high) / 2
    delta = (x_low + x_high) / 4
    for i in range(n):
        k = x_mid ** 2 - alpha
        if k < 0:
            x_mid += delta
        else:
            x_mid -= delta
        delta /= 2
    return(x_mid)


for i in range(15):
    root = find_root(9, i)
    print(i, root, abs(root - 3))
