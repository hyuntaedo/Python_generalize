from bs4 import BeautifulSoup
import requests
url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0+"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# requtest를 써봐야함
# with open("quiz.html", "w", encoding="utf8") as f:
#    f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class": "tbl"}).find(
    "tbody").find_all("tr")
for index, row in enumerate(data_rows):
    colums = row.find_all("td")

    print("===매물{}===".format(index+1))
    print("거래 : ", colums[0].get_text().strip())
    print("면적 : ", colums[1].get_text().strip(), "(공급/전용)")
    print("가격 : ", colums[2].get_text().strip(), "민원")
    print("동 : ", colums[3].get_text().strip())
    print("층 : ", colums[4].get_text().strip())
