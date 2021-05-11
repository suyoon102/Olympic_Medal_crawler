import matplotlib.pyplot as plt
import matplotlib
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://gsic.sports.or.kr/com/cop/game/game_info.do?partCode=1&gameCode=145")

soup = BeautifulSoup(html, "lxml")

chart_table = soup.find_all('table',{'class':'table_t boardList selection'})

chart_table_tbody=chart_table[0].find_all("tbody")

chart_table_tr=chart_table_tbody[0].find_all("tr")

tr_list=[]
for i in chart_table_tr:
    td = i.find_all('td')
    tr_list.append(i.get_text())

rank=[]
country=[]
gold=[]
silver=[]
bronze=[]
sum_medal=[]
for i in tr_list:
    str=i.split('\n')
    del str[-1]
    del str[0]
    print(str)
    country.append(str[1])
    gold.append(int(str[2]))
    silver.append(int(str[3]))
    bronze.append(int(str[4]))
    sum_medal.append(int(str[5]))

print(rank)
print(country)
print(gold)
print(silver)
print(bronze)
print(sum_medal)

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
x=np.arange(30)
print(x)
print(gold[:30])
plt.bar(x,gold[:30])
plt.xticks(x,country[:30],rotation='vertical')
plt.show()
plt.xticks(country)