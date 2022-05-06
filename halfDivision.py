segment = [-1.5, -1]

def f(x):
    return -1.85 * x ** 3 - 4.75 * x ** 2 - 2.53 * x + 0.49

while True:
    print("a: ", segment[0])
    print("b: ", segment[1])
    print("x: ", (segment[0]+segment[1]) / 2)
    print("f(a): ", f(segment[0]))
    print("f(b): ", f(segment[1]))
    print("f(x): ", f((segment[0]+segment[1]) / 2))
    print("|a-b|: ", abs(segment[0] - segment[1]))
    print("\n")

    if not (abs(f((segment[0] + segment[1]) / 2)) > 0.01 or abs(segment[0] - segment[1]) > 0.01):
        break

    if (f((segment[0]+segment[1]) / 2) > 0 and f(segment[0]) > 0) or (f((segment[0]+segment[1]) / 2) < 0 and f(segment[0]) < 0):
        segment[0] += abs(segment[0] - segment[1]) / 2
    else:
        segment[1] -= abs(segment[0] - segment[1]) / 2