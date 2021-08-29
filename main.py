def prim(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d=3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

n = int(input())
r = prim(n)
if r:
    print("Este prim.")
else:
    print("Nu este prim.")