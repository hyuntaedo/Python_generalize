#어떤 수 N이 1이될때 까지 다음으 두 과정중 하나를 반복함
# N에서 1을 뺀다
# N을 K로 나눈다
# N = 17 K=4 -> 1번수행 시 N=16이됨
n,k = map(int,input().split())
count = 0
while True:
    target = (n//k) *k #k로 나누어 떨어지는 수
    count += (n-target)
    n = target

    if n<k:
        break
    count +=1
    n //= k

count += (n-1)
print(count) 

