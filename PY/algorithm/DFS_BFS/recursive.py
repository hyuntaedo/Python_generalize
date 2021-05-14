#recursive란 자기 자신을 다시 호출하는 함수
def recursive_function(i):
    if i == 100: #종료 조건을 명시
        return
    print(i,"재귀함수를 호출",i+1,'번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print("{0}번째 재귀함수를 종료합니다.".format(i))
    #최대 깊이 제한이 있음
    #오류가 안뜰려면 따로 stack을 만들어야함
    #while이나 for을 사용하지않고 재귀함수를 사용할 수 있음
    #단점은 자기 함수를 다시 호출하는것이기때문에 스택메모리에 계속 쌓임
    #메모리가 비효율적일 수 있으나 time complexity는 큰 차이가없음
recursive_function(1)
