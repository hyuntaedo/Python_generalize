from selenium import webdriver
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 해상도 1920X1080으로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)")
# browser.execute_script("window.scrollTo(0,1080)")

# 화면 가장 아래로 스크롤 내리기
browser.execute_async_script("window.scrollTo(0,document.body.scrollHeight)")


interval = 2  # 2초에 한번씩 스크롤을 내림

# 현재 문서 높이 저장
previous_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_async_script(
        "window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 저장
    current_height = browser.execute_async_script(
        "window.scrollTo(0,document.body.scrollHeight)")
    if current_height == previous_height:
        break
    # 높이 업데이트
    previous_height == current_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")

# 동적 페이징

soup = BeautifulSoup(browser.page_source, "lxml")

#movies = soup.find_all("div", attrs={"class": ["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})

print(len(movies))  # 왜 0개인가?

for movie in movies:
    title = movie.find("span", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title, "할인되지 않은 가격입니다.")
        continue

    # 할인 된 가격
    price = movie.find(
        "span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크 정보
    link = movie.find("a", attrs={"class": "ZC71ub"})["href"]
    # play.google.com을 생성해야지 올바른 정보가 생성됨
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print(f"link : ", "https://play.google.com" + link)
    print("-"*100)

browser.quit()
