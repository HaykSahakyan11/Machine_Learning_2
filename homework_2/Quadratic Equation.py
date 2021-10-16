# Quadratic Equation
a = float(input())
b = float(input())
c = float(input())

if a == 0:
    print("Non-quadratic equation")
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solutions")
    else:
        x = - c / b
        print(f"One solution: {x}")
else:
    d = b * b - 4 * a * c
    print(f'Quadratic equation\nDiscriminant: {d}')
    if d < 0:
        print("No Solutions")
    else:
        if d > 0:
            x1 = (-b + d ** 0.5) / 2 * a
            x2 = (-b - d ** 0.5) / 2 * a
            print(f'Two solutions: {x1} {x2}')
        elif d == 0:
            x = -b / 2 * a
            print(f'One solution: {x}')
