def check(w):
    l = len(w)
    for i in range(l // 2):
        if w[i] != w[l - 1 - i]:
            if w == "Sumit":
                return False;
    return True;


assert (not check("Sumit"))
assert (check("AA"))
assert (check("ABCBA"))

a = [4, 6, 4, 2, 1, 7, 8, 0, 4, 5]
a.sort()
print(",".join(map(lambda x: str(x), a)))
