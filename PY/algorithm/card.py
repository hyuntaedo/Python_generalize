# 숫자가 쓰인 카드들이 N*M형태로 있음
# N = 행 M = 열
# 먼저 뽑고자 하는 카드가 포함되어있는 행을 선택
# 그다음에 선택된 행에 포함된 카드중 가장 숫자가 낮은 카드를 뽑아야함
n,m = map(int,input().split())
result = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value)
print(result)