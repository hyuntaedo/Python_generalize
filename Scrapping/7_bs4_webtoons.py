#정보를 다 긁어오기
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

#naver웹툰 전체 목록 가져오기
cartoons = soup.find_all("a",attrs={"class":"title"})#모든 element를 가져옴
#a element의 class속성이 title인 모든 element를 반환
for cartoon in cartoons:
    print(cartoon.get_text())

