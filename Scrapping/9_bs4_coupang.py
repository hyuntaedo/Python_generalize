#get방식 -> url에 적음(보안강도 약함)
#post -> http body에 섞어서 보냄(보안강도 강함)
import requests
import re
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
print(res.text)

items = soup.find_all("li",attrs={"class":re.compile("^search-product")})
print(items[0].find("div",attrs={"class":"name"}).get_text())
for item in items:

    #광고제품 제외
    ad_badge = item.find("span",attrs={"class":"ad-badge-texet"})
    if ad_badge:
        print("<광고상품 제외합니다.>")
        continue

    name = item.find("div",attrs={"class":"name"}).get_text()
    #애플 제품 제외

    if "Apple" in name:
        print(" <Apple>상품 제외합니다.")
        continue

    price = item.find("strong",attrs={"class":"price-value"}).get_text()
    
    #리뷰 100개이상 평점 4.5이상
    rate = item.find("em",attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점없음"
    rating = item.find("span",attrs={"class","rating-total-count"})
    if rating:
        rating = rating.get_text()
        rating = rating[1:-1]
    else:
        rating = "평점 수 없음"
        print("<평점 수가 없는 상품을 제외합니다.>")
        continue

    if float(rate) >=4.5 and int(rating) >= 100:
        print(name,price,rate,rating)
    
