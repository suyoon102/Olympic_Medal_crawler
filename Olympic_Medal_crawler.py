from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://gsic.sports.or.kr/com/cop/game/game_info.do?partCode=1&gameCode=145")

soup = BeautifulSoup(html, "lxml")

chart_table = soup.find_all('table',{'class':'table_t boardList selection'}) #메달 통계가 적힌 테이블 불러와 변수에 저장

chart_table_tbody=chart_table[0].find_all("tbody") #순위   국가   금메달   은메달   동메달   합계 라고 되어있는 부분 제외밑 통계부분 불러오기