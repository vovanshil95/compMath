segment = [0, 0.5]

def f(x):
    return -1.85 * x ** 3 - 4.75 * x ** 2 - 2.53 * x + 0.49

while True:
    print("x_k-1: ", segment[0])
    print("f(x_k-1): ", f(segment[0]))
    print("x_k:", segment[1])
    print("f(x_k): ", f(segment[1]))
    print("x_k+1: ", segment[1]-(segment[1]-segment[0])/(f(segment[1])-f(segment[0]))*f(segment[1]))
    print("f(x_k+1): ", f(segment[1]-(segment[1]-segment[0])/(f(segment[1])-f(segment[0]))*f(segment[1])))
    print(abs(segment[1] - (segment[1]-(segment[1]-segment[0])/(f(segment[1])-f(segment[0]))*f(segment[1]))))
    print("\n")

    if abs(segment[1] - segment[0]) < 0.01 and abs(f(segment[1])) < 0.01:
        break

    segment[0], segment[1] = segment[1], segment[1] - (segment[1] - segment[0]) / (f(segment[1]) - f(segment[0])) * f(segment[1])
