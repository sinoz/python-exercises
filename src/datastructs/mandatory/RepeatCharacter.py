def repeat(character, n):
    res=""
    while((n > 0)):
        res=(res+character)
        n=(n-1)
    return res

res=repeat("#", 6)
print(res)