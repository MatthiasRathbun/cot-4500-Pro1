def approximate_root_two(tol=0.000001):
    x0 = 1.5
    x = x0
    iter = 0
    diff = x0

    while diff >= tol:
        iter += 1
        y = x
        x = (x / 2) + (1 / (x))
        diff = abs(x - y)
        print(f"{iter} : {x}")

    print(f"\nConvergence after {iter} iterations")
    return x

def bisection_method(f, a, b, tol, max_iter):
    left, right = a, b
    i = 0

    while abs(right - left) > tol and i < max_iter:
        i += 1
        p = (left + right) / 2.0

        if f(left) * f(p) < 0:
            right = p
        elif f(left) * f(p) > 0:
            left = p
        else:
            break  # Found exact solution

    return p

def fixed_point_iteration(g, p0, TOL, N0):
    i = 1
    while i <= N0:
        p = g(p0)
        if abs(p - p0) < TOL:
            return p, "SUCCESS"
        i += 1
        p0 = p
    return 0, "FAILURE"

def newton_method(f, df, p0, TOL, N0):
    i = 1
    while i <= N0:
        if df(p0) != 0:
            p = p0 - f(p0) / df(p0)
            if abs(p - p0) < TOL:
                return p, "SUCCESS"
            i += 1
            p0 = p
        else:
            return 0, "FAILURE DERIVATIVE IS ZERO"
    return 0, "FAILURE MAX ITTERATIONS PERFORMED"