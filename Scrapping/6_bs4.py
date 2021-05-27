#beautifulsoup4 -> 스크래핑 모듈
#lxml -> 구문분석 모듈
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
#print(soup.title)
#print(soup.title.get_text())#title태그 받아오기
#print(soup.a) #a soup객체에서 처음발견되는 a element를 받아옴
#print(soup.a.span.get_text())#a태그 받아오기
#print(soup.a.attrs)# 속성
#print(soup.a["href"])# href를 받아옴

#print(soup.find("a",attrs={"class":"Nbtn_upload"}))
#print(soup.find(attrs={"class":"Nbtn_upload"})) #class가 Nbtn_uploadㅇ인 버튼을 찾아줌
#print(soup.find("li",attrs={"class":"rank01"}))
rank1 = soup.find("li",attrs={"class":"rank01"})
#print(rank1.a)

#print(rank1.a.get_text())
#rank2 = rank1.next_sibling.next_sibling #줄바꿈이 있는것
#rank3 = rank2.next_sibling.next_sibling #내 다음위치의 관계로 넘어감
#print(rank3.get_text())
#rank2 = rank3.previous_sibling.previous_sibling
#print(rank2.a.get_text())
#print(rank1.parent)
#rank2 = rank1.find_next_sibling("li") #개행과 상관없이 li에 해당하는 태그만 받아옴
#print(rank2.a.get_text())
#rank3 = rank2.find_next_sibling("li")
#print(rank3.a.get_text())
#rank2 = rank3.find_previous_sibling("li")
#print(rank2.a.get_text())
#한번에 정보를 찾기
#print(rank1.find_next_siblings("li"))

webtoon = soup.find("a",text="신의 탑 3부-69화")
print(webtoon)

