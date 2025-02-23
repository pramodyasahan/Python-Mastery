def generate():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


g = generate()
# print(sum(g)) output: 15

for _ in range(5):
    value = next(g)
    print(value)
