def repeat(symbol, n):
    res=""
    while((n>0)):
        res=(res+symbol)
        n=n-1
    return res

def draw_line(n):
    return repeat("*", n)

def draw_empty_square(n):
    l=(draw_line(n) + "\n")
    empty_line=("*" + (repeat(" ", (n - 2)) + "*\n"))
    return l + (repeat(empty_line, (n - 2))) + l

res=draw_empty_square(4)
print(res)