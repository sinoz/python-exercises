def repeat(symbol, n):
    res=""
    while n>0:
        res=(res+symbol)
        n=(n-1)
    return res

def draw_line(n):
    return repeat("*", n)

def draw_square(n):
    l=(draw_line(n) + "\n")
    return repeat(l, n)

res=draw_square(6)
print(res)