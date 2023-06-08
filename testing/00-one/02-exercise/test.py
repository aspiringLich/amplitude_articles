
def test_add(ctx):
    a = ctx.randint(-100, 100)
    b = ctx.randint(-100, 100)
    ctx.input(0, a)
    ctx.input(1, b)
    ctx.output(a + b)
