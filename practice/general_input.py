import sys
#print("python","java",file=sys.stdout) #출력
#print("python","java",file=sys.stderr) #error 처리


#scores = {"수학":0,"영어":50,"코딩":100}
#for subject, score in scores.items(): # key, value를 쌍으로 튜플로 보내줌
#    print(subject.ljust(8),str(score).rjust(4),sep=":") #ljust는 왼쪽정렬
    #(8)은 8개의 공간을 만들고 난 다음에 정렬을 한다는 뜻

#print("python","java", sep=",",end="?") 
# sep안의 값을 선언하면 " "안의값이 찍힌다 
# end는 안의 문장을 출력되게한다
#print("\n무엇이 더 재밌을 까요")

#은행 대기 순번표
#001,002,003...
#for number in range(1,21):
#    print("대기번호 : " + str(number).zfill(3))
    #zfill은 값이 없는 빈 공간은 0으로 채워달라는 말임

#표준입력
answer = input("아무값이나 입력하세요 : ")
answer = 10
print(type(answer))
print("입력하신 값은 " + answer + "입니다")
#사용자 값으로 받은 값은 무조건 문자열로 드가진다