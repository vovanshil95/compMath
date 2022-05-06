segment = [-2, -1.5]

q = 0.4
x = -2

def fi(x):
    return (-1.85 * x ** 3 - 4.75 * x ** 2 + 0.49) / 2.53

def f(x):
    return -1.85 * x ** 3 - 4.75 * x ** 2 - 2.53 * x + 0.49


while True:
    print("x_k: ", x)
    print("f(x_k): ", f(x))
    print("x_k+1: ", fi(x))
    print("fi(x_k): ", fi(x))
    print("|x_k-x_k+1|: ", abs(x-fi(x)))
    print("\n")

    if abs(x - fi(x)) < 0.01:
        break

    x = fi(x)