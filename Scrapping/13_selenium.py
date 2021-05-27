from selenium import webdriver
import time
browser = webdriver.Chrome()

# 1번 네이버로 이동
browser.get("https://www.naver.com")

# 2번 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3번 id,pwd입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

# 4번 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
time.sleep(3)
# 5번 id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")


# 6번 html정보 출력
print(browser.page_source)


# 7번 브라우저 종료
browser.quit()  # 전체 종료
# browser.close() 현재 탭만 종료
