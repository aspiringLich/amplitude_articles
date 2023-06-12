
def gen_add(ctx):
    a = ctx.randint(-100, 100)
    b = ctx.randint(-100, 100)
    ctx.inputs([a, b])
    ctx.output(a + b)
