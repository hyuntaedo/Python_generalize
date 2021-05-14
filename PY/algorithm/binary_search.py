#분할 정복법
#이분검색(BINARY_SEARCH)
##n = map(int,input().split())
#n = list(map(int,input().split()))
#n.sort()

#1. 임의의 중간 인덱스 값을 구함
#2. 절반씩 줄어들면서 찾아가야함

def location(S,low,high):
    if(low>high):
        return 0
    else:
        mid = (low + high) //2
        if(x == S[mid]):
            return mid
        elif (x<S[mid]):
            return location(S,low,mid-1)
        else:
            return location(S,mid+1,high)

S = [-1,10,12,13,14,17,18,20,25,30,35,40,45]
x = 18
loc = location(S,1,len(S)-1)
print("S = ",S)
print("x = ",x)
print("loc = ",loc)