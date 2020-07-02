#!/usr/bin/env python
# coding: utf-8

# In[43]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
from datetime import datetime


# In[44]:


url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=&brdGubun=&ncvContSeq=&contSeq=&board_id=&gubun="
html = urlopen(url)
source = html.read() # 바이트코드 type으로 소스를 읽는다.
html.close() # urlopen을 진행한 후에는 close를 한다

soup = BeautifulSoup(source, "html.parser") # 파싱할 문서를 BeautifulSoup 클래스의 생성자에 넘겨주어 문서 개체를 생성, 관습적으로 soup 이라 부름
keywords = soup.find_all('td',class_='w_bold') # 데이터에서 태그와 클래스를 찾는 함수
keywords = [each_line.get_text().strip() for each_line in keywords[:20]]
data=list()
data.extend(keywords)


# In[45]:


data[0]=data[0][:-2]
data[1]=data[1][:-2]
data[2]=data[2][:-2]
data[3]=data[3][:-1]  ##주의

data[0] = data[0].replace(',', '')
data[1] = data[1].replace(',', '')
data[2] = data[2].replace(',', '')
data[3] = data[3].replace(',', '')


# In[46]:


url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="
html = urlopen(url)
source = html.read() # 바이트코드 type으로 소스를 읽는다.
html.close() # urlopen을 진행한 후에는 close를 한다

soup = BeautifulSoup(source, "html.parser") # 파싱할 문서를 BeautifulSoup 클래스의 생성자에 넘겨주어 문서 개체를 생성, 관습적으로 soup 이라 부름
keywords2 = soup.find_all('td',class_='number') # 데이터에서 태그와 클래스를 찾는 함수
keywords2 = [each_line.get_text().strip() for each_line in keywords2[:20]]
data2=list()
data2.extend(keywords2)


# In[47]:


conn = pymysql.connect(host='localhost', user = 'root', password='dldbrud12!', db = 'corona',charset = 'utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

now = datetime.now()
newdate = now.strftime('%m/%d -%I %p')

x = data[0]
y = data[1]
z = data[2]
w= data[3]
a=data2[0]


sql = "update people set ill=%s, clean = %s, death=%s, ing=%s, date=%s,newill=%s " 

curs.execute(sql,(x,y,z,w,newdate,a))

conn.commit()

conn.close()


# In[48]:


url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="
html = urlopen(url)
source = html.read() # 바이트코드 type으로 소스를 읽는다.
html.close() # urlopen을 진행한 후에는 close를 한다

soup = BeautifulSoup(source, "html.parser") # 파싱할 문서를 BeautifulSoup 클래스의 생성자에 넘겨주어 문서 개체를 생성, 관습적으로 soup 이라 부름
keywords = soup.find_all('td',headers='status_con s_type2') # 데이터에서 태그와 클래스를 찾는 함수
keywords = [each_line.get_text().strip() for each_line in keywords[:20]]

keywords1 = soup.find_all('td',headers='status_con s_type3') # 데이터에서 태그와 클래스를 찾는 함수
keywords1 = [each_line.get_text().strip() for each_line in keywords1[:20]]

keywords2 = soup.find_all('td',headers='status_con s_type4') # 데이터에서 태그와 클래스를 찾는 함수
keywords2 = [each_line.get_text().strip() for each_line in keywords2[:20]]

keywords3 = soup.find_all('td',headers='status_test s_type6') # 데이터에서 태그와 클래스를 찾는 함수
keywords3 = [each_line.get_text().strip() for each_line in keywords3[:20]]

data=list()
data.extend(keywords)


data1=list()
data1.extend(keywords1)


data2=list()
data2.extend(keywords2)


data3=list()
data3.extend(keywords3)


# In[49]:


for i in range(1,18):
    data[i] = data[i].replace(',', '')
    data1[i] = data1[i].replace(',', '')
    data2[i] = data2[i].replace(',', '')
    data3[i] = data3[i].replace(',', '')


# In[50]:


conn = pymysql.connect(host='localhost', user = 'root', password='dldbrud12!', db = 'corona',charset = 'utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)


for i in range(1,18):
    sql = "update city set ill=%s where num=%s" 
    curs.execute(sql,(data[i],i))  
    sql = "update city set clean=%s where num=%s" 
    curs.execute(sql,(data1[i],i))
    sql = "update city set death=%s where num=%s" 
    curs.execute(sql,(data2[i],i))
    sql = "update city set ing=%s where num=%s" 
    curs.execute(sql,(data3[i],i))

conn.commit()

conn.close()


# In[51]:


url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
html = urlopen(url)
source = html.read() # 바이트코드 type으로 소스를 읽는다.
html.close() # urlopen을 진행한 후에는 close를 한다

soup = BeautifulSoup(source, "html.parser") 
conn = pymysql.connect(host='localhost', user = 'root', password='dldbrud12!', db = 'corona',charset = 'utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

world = soup.find_all('td',class_='w_bold') # 데이터에서 태그와 클래스를 찾는 함수
world = [each_line.get_text().strip() for each_line in world]


world_list=list()
world_list.extend(world)

world_list = world_list[4:67]

for i in range(0,63):
    sql="UPDATE `world` SET `name`=%s where num=%s"
    curs.execute(sql,(world_list[i],(i+1)))

conn.commit()

conn.close()


# In[52]:


url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
html = urlopen(url)
source = html.read() # 바이트코드 type으로 소스를 읽는다.
html.close() # urlopen을 진행한 후에는 close를 한다

soup = BeautifulSoup(source, "html.parser") 
conn = pymysql.connect(host='localhost', user = 'root', password='dldbrud12!', db = 'corona',charset = 'utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

world = soup.find_all('td') # 데이터에서 태그와 클래스를 찾는 함수
world = [each_line.get_text().strip() for each_line in world]


world_list=list()
world_list.extend(world)


world_list = world_list[4:130]

world_list2=list()
world_list3=list()

for i in range(0,63):
    world_list2.append(world_list[2*i+1])
    world_list3.append(world_list[2*i+1])

for i in range(0,63):
    world_list2[i] = world_list2[i].replace(',', '')
    world_list3[i] = world_list2[i].replace(',', '')
        
str = '명'
str1 = ' '
str2 = ')'

for i in range(0,63):
    a = world_list2[i].find(str)
    if a!=-1:
        world_list2[i] = world_list2[i][:a]
    b = world_list3[i].find(str1)
    if b!=-1:
        world_list3[i] = world_list3[i][b+1:]
    c = world_list3[i].find(str2)
    if c!=-1:
        world_list3[i] = world_list3[i][:c]
        a = world_list3[i].find(str)
    if a!=-1:
        world_list3[i] = ''
        
for i in range(0,63):
    sql="UPDATE `world` SET `ill`=%s,`death`=%s WHERE num=%s"
    curs.execute(sql,(world_list2[i],world_list3[i],(i+1)))

conn.commit()

conn.close()


# In[ ]:


conn = pymysql.connect(host='localhost', user = 'root', password='dldbrud12!', db = 'corona',charset = 'utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

now = datetime.now()
formatted_date = now.strftime('%m/%d -%I %p')
sql = "update people set date=%s " 

curs.execute(sql,formatted_date)

conn.commit()

conn.close()


# In[ ]:





# In[ ]:





# In[ ]:




