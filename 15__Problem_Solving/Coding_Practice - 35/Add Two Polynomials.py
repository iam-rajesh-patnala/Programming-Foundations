def take_polymonial():
    n = int(input())
    p = {}
    for i in range(n):
        L = input().split()
        Pi = int(L[0])
        Ci = int(L[1])
        p[Pi] = Ci
    return p


def add_polynomials(p, q):
    r = {}
    Pis = set(p).union(q)
    for Pi in Pis:
        if Pi in p:
            Ci = p[Pi]
        else:
            Ci = 0.0
        if Pi in q:
            Ci += q[Pi]

        if Ci != 0.0:
            r[Pi] = Ci
    return r


def tostring_polynom(p):
    res = ""
    first = True
    for Pi in sorted(p, reverse=True):
        Ci = p[Pi]
        if first:
            if Ci == 0 and Pi == 0:
                return "0"

            if Ci == 1 and Pi != 0:
                pass
            elif Ci == -1 and Pi != 0:
                res = "-"
            else:
                res = f"{int(Ci)}"
            first = False

        else:
            if Ci > 0:
                res += " + "
            elif Ci < 0:
                res += " - "
            else:
                continue
            if abs(Ci) != 1:
                res += f"{abs(int(Ci))}"

        if Pi == 0:
            continue
        if Pi == 1:
            res += "x"
        else:
            res += f"x^{Pi}"

    if res == "":
        res += "0"
    if res[-1] == " ":
        res += "1"
    return res


p = take_polymonial()
q = take_polymonial()

r = add_polynomials(p, q)

result = tostring_polynom(r)

print(result)
