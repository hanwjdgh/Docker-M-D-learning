from selenium import webdriver

# PhantomJS 드라이버 추출
browser = webdriver.PhantomJS()
# 3초 대기하기
browser.implicitly_wait(3)

# url 읽어 들이기
browser.get("http://nid.naver.com/nidlogin.login")
# 로그인
element_id = browser.find_element_by_id("id")
element_id.clear()
element_id.send_keys("ID")
element_pw = browser.find_element_by_id("pw")
element_pw.clear()
element_pw.send_keys("PW")

# 화면을 캡처해서 저장하기
browser.save_screenshot("Website_C.png")

button = browser.find_element_by_css_selector("input.btn_global[type=submit]")
button.submit()

#메일페이지 열기
browser.get("https://mail.naver.com/")
browser.save_screenshot("Website_D.png")
titles = browser.find_elements_by_css_selector("strong.mail_title")

for title in titles:
    print(title.text)

# 브라우저 종료하기
browser.quit()