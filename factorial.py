
def factorial(number):
    def inter(num, val):
        if num == 1:
            return val
        else:
            return inter(num - 1, val * num)

    return inter(number, 1)


print(factorial(5))
