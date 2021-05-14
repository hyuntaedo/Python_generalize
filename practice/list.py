subway1 = 10
subway2 = 20
subway3 = 30
subway = [10,20,30]
print(subway)
subway = ['a','b','c']
#b의 위치를 찾음
print(subway)
print(subway.index('b'))
#맨 뒤에 삽입
subway.append('d')
print(subway)
#중간에 삽입
subway.insert(1,'h')
print(subway)

#뒤에서 꺼냄
subway.pop()
print(subway)

#같은 문자가 몇개 있는지 확인
subway.append('a')
print(subway.count('a'))

#sorting
num_list = [5,1,2,3,4]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)

#clear
num_list.clear()
print(num_list)

#자료형에 구애받지 않음
mix_list = ['a',1,True]
print(mix_list)

#list 확장
num_list.extend(mix_list)
