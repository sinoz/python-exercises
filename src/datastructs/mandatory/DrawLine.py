def draw_line(n):
    res=""
    while((n>0)):
        res=(res+"*")
        n=(n-1)
    return res

res = draw_line(5)
print(res)