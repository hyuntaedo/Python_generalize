#재귀함수 facotiral_recursive
def factoral(n):
    if n<=1:
        return 1
    return n * factoral(n-1)
print("반복적으로 구현",factoral(5))
