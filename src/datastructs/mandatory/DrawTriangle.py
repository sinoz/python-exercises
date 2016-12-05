def repeat(symbol, n):
    res=""
    while((n>0)):
        res=(res+symbol)
        n=(n-1)
    return res

def draw_line(n):
    return repeat("*", n)

def draw_triangle(n):
    if((n <= 0)):
        return ""
    else:
        return draw_line(n) + ("\n" + draw_triangle((n - 1)))

res=draw_triangle(4)
print(res)