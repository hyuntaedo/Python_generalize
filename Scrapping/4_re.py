# 정규식 = 정해진형태를 의미함
# 주민등록번호, email...
import re  # 정규식
p = re.compile("ca.e")  # 하나의 문자를 의미
# .(ca.e)은 하나의 문자를 의미 > care,cafe,case...
# ^(^de)는 문자열의 시작을 의미 > desk,destination...
# $(se$)는 문자열의 끝을 의미 > case,base...


def print_match(m):
    # print(m.group()) #매치되지 않으면 에러 발생
    if m:
        print("m.groupe() :", m.group())
        print("m.string() :", m.string)
        print("m.start() :", m.start())  # 일치하는 문자열의 시작 index
        print("m.end() :", m.end())  # 일치하는 문자열의 끝index
        print("m.span() : ", m.span())  # 일치하는 문자열의 시작/끝 index
    else:
        print("매칭되지않았습니다.")
# m = p.match("case") #match : 주어진 문자열의 처음부터 일치하는지 확인하는것
# print_match(m)

# m = p.search("careless") #search : 주어진 문자열중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("good care cafe") #findall : 일치하는 모든것을 리스트형태로 반환
# print(lst)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터
# 3. m = p.search("비교할 문자열") : 일치하는게 있는지
# 4. m = p.findall("비교할 문자열") : 일치하는 모든것을 리스트형태로 반환

# 정규식 : . => 하나의 문자 ^ => 문자열의 시작 $ => 문자로 끝나는것
