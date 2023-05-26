import random

random.seed(857398)

def gen_add(ctx):
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    ctx.input(0, a)
    ctx.input(1, b)
    ctx.output(a + b)
