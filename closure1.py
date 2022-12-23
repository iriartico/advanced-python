def make_multiplier(x):

    def multiplier(n):
        return x * n

    return multiplier


time10 = make_multiplier(10)
time4 = make_multiplier(4)

print(time10(3))
print(time4(5))
print(time10(time4(2)))
