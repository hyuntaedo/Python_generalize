#file 입출력
#score_file = open("score.txt","w",encoding="utf8")
#print("수학점수는 : 0",file=score_file)
#print("영어점수는 : 50",file=score_file)
#score_file.close()


#append는 이어쓰는것 "a"
#score_file.write()는 줄바꿈이 없음
#score_file = open("score.txt","a",encoding="utf8")
#score_file.write("과학 : 80")
#score_file.write("\n코딩 : 100")


#read
#score_file = open("score.txt","r",encoding="utf8")
#print(score_file.read())
#score_file.close()

#한줄씩 불러오기
#score_file = open("score.txt","r",encoding="utf8")
#print(score_file.readline(),end="")#한줄 씩 불러옴, 커서는 다음 줄로 이동함
#print(score_file.readline(),end="")
#print(score_file.readline(),end="")
#print(score_file.readline(),end="")
#score_file.close()

#총 몇줄 인지 모를 때(반복문으로 불러옴)
#score_file = open("score.txt","r",encoding="utf8")
#while True:
#    line = score_file.readline()
#    if not line:
#        break
#    print(line)
#score_file.close()

#list에다 값을 넣어서 처리
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() #모든 라인을 리스트로 저장함
for line in lines:
    print(line,end="")
score_file.close()
