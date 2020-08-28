def permute(s, l):
    if s == 1:
        return l
    else:
        return [x + y
                for x in permute(1, l)
                for y in permute(s - 1, l)
                ]


print(permute(1, ["a", "b", "c"]))
print(permute(3, ["a", "b", "c"]))
