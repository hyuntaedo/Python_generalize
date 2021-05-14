#전역변수 = 모든공간
#지역변수 = 그 함수 안에서만
gun = 10
def checkpoint(soldier):
    #여기서 초기화가 안되서 오류가 난다. (지역변수)
    global gun # 이걸 적어주면 글로벌변수의 총을 가져와서 쓴다
    gun = gun - soldier
    print("[함수 내]에서 남은 총{0}".format(gun))

def checkpoint_return(gun,soldier):
    gun = gun-soldier
    print("[함수 내]에서 남은 총{0}".format(gun))
    return gun
    

print("전체 총의 수 : {0}".format(gun))# 글로벌 변수의 총
checkpoint(2)
print("남은 총 : {0}".format(gun)) #로컬변수 내의 총
#가급적 파라미터로 던져서 계산을 하고 반환을 받아서 사용함
gun = checkpoint_return(gun,2)
print("남은 총 : {0}".format(gun)) #로컬변수 내의 총
