#def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#   print("이름 : {0}\t나이:{1}\t".format(name,age),end=" ")
#    print(lang1,lang2,lang3,lang4,lang5)

profile("김","20","python","java","js","c++","c#") # 할줄아는게 하나 더 있으면 함수를 하나 더 바꿔야함
profile("이","23","Kotlin","Swift","","","") #빈 값을 넣어줘야함
#여기서 가변인자를 쓸 수 있음

def profile(name,age,*lang):
    print("이름 {0}\t나이{1}".format(name,age),end=" ")
    for lang in language:
        print(lang,end=" ")
    print()
profile("김",20,"py","js","c","c++","c#","c-obj")
profile("이",23,"kotlin","swift")    