n,m,k = map(int,input().split()) # 입력
data = list(map(int,input().split())) #리스트에 데이터 삽입
data.sort() #소팅
first = data[n-1] #가장 큰 수 
second = data[n-2] # 두번 째로 큰 수
result = 0 #결과값 초기화

while(True):
    for i in range(k): #더하는 횟수만큼 반복
        if m ==0: # 더하는게 끝났다면 
            break
        result += first # 값 입력
        m -=1 #m을 감소시키고
    if m==0: # 그다음으로 큰 수가 0이된다면
        break
    result += second # 값 입력
    m -=1

print(result)