def juclid(a,b):
    if a%b ==0:
        return b
    else:
        return juclid(b, a%b)

print(juclid(192, 162))
