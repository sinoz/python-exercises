def draw_grid(x_dim, y_dim, p):
    res = ""
    x = 0
    y = 0
    while ((y < y_dim)):
        while ((x < x_dim)):
            if (p(x, y)):
                res = (res + "#")
            else:
                res = (res + "_")
            x = (x + 1)
        res = (res + "\n")
        x = 0
        y = (y + 1)
    return res

NOT = lambda p: lambda x, y: (not p(x, y))
left = lambda x, y: (x == 0)
right = NOT(left)
res = draw_grid(4, 4, left)
print(res)