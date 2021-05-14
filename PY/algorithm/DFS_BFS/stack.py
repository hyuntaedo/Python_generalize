#자주 나옴
#stack = 먼저 들어온데이터가 나중에 나감
#선입후출(5 2 3 7 del(7) 1 4 del(4)  )이라고도 하는데 입구와 출구가 동일한 형태
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])
#최상단 원소부터
print(stack)
#최하단 원소부터