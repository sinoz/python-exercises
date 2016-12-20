def draw_grid(x_dim, y_dim, p):
    res = ""
    x = 0
    y = 0
    while ((y < y_dim)):
        while ((x < x_dim)):
            if (p(x, y)):
                res = (res + "*")
            else:
                res = (res + "_")
            x = (x + 1)
        res = (res+"\n")
        x = 0
        y = (y + 1)
    return res

print(draw_grid(3, 3, lambda x, y: y >= 0))