
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from bs4 import BeautifulSoup

# 이미지를 바이트 변환 처리 모듈
from io import BytesIO

# 엑셀 처리 모듈 임포트
import xlsxwriter

#user-agent 정보를 전환해 주는 모듈 임포트
# 특정 브라우저로 크롤링을 진행할 때 차단되는 것을 방지
from fake_useragent import UserAgent

# 요청 헤더 정보를 꺼내올 수 있는 모듈
import urllib.request as req


d = datetime.today()

file_path = f'/Users/dood/Desktop/java_web_JS/python/crawling/멜론 차트 1~100_{d.year}_{d.month}_{d.day}.xlsx'

opener = req.build_opener()
opener.addheaders = [('User-agent', UserAgent().random)]
req.install_opener(opener)

workbook = xlsxwriter.Workbook(file_path)

worksheet = workbook.add_worksheet()

chrome_option = Options()
chrome_option.add_argument('--headless')

# 브라우저 설정 - headless 모드
driver = webdriver.Chrome('/Users/dood/Desktop/java_web_JS/python/chromedriver', options=chrome_option)

# 브라우저 사이즈 조정
driver.set_window_size(800, 600)

# 브라우저 내부 대기
# time.sleep(10) -> 브라우저 로딩에 상관없이 무조건 10초 대기

# 웹 페이지 전체가 로딩될 때 까지 대기 후 남은 시간 무시.
driver.implicitly_wait(10)

# 페이지 이동 (멜론 차트 페이지)
driver.get('https://www.melon.com/chart/day/index.htm')

cell_format = workbook.add_format({'bold:True'})
worksheet.write('A1', '순위', cell_format)
worksheet.write('B1', '커버사진', cell_format)
worksheet.write('C1', '가수이름', cell_format)
worksheet.write('D1', '앨범명', cell_format)
worksheet.write('E1', '노래명', cell_format)

cur_page_num = 2
target_page_num = 5
rank = 1
cnt = 2

worksheet.set_column('A:E', 25)

while True:

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    div_service_list_song = soup.find_all('div', class_='wrap_song_info')

    for div_wrap_song_info in div_service_list_song:

        # 이미지
        img_url = div_wrap_song_info.select_one('td > a img.image_typeAll')

        #
        td = div_wrap_song_info.select_one('div_service_list_song > td')

        #
        title = td.select_one('div > ellipsis rank01 ')


