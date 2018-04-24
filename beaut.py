from bs4 import BeautifulSoup

html="""
<html>
    <boby>
        <div id="meigen">
            <h1>도서</h1>
            <ul class="items">
                <li>유니티 게임 이펙트 입문</li>
                <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                <li>모던 웹사이트 디자인의 정석</li>
            </ul>
        </div>
    </body>
</html>
"""

# "태그 이름" 태그 선택자
# #<아이디 이름> ID 선택자
# .<클래스 이름> class 선택자
# 후손 선택자 ex) html 밑 모든것 -> html li
# 자식 선택자 ex) html 바로 밑 -> html > body

soup = BeautifulSoup(html,'html.parser')

header = soup.select_one("div > h1")
list_items = soup.select("ul.items > li")

print(header.string)
#header.attrs["title"]
print(soup.select_one("ul").attrs)
for li in list_items:
    print(li.string)