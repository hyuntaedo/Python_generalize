kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

# 1,1 index 2,2 index, 3,3 index 끼리 합쳐줌
zip(kor, eng)

print(list(zip(kor, eng)))

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
# 다시 분리해줌
print(list(zip(*mixed)))

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)
