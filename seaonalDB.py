import urllib.request
from bs4 import BeautifulSoup
import mysql.connector

def parse_seaonal(url) :
    rows=[]
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}
    months = ['0'+str(m) for m in range(1,10)]
    months.extend(['10','11','12'])

    for year in [2018] : ##, 2017,2016, 2015] :
        for month in range(1,13) :
            if len(str(month)) ==1 : m = '0' + str(month)
            else : m = str(month)
            parse_url = url + '&thisYear='+str(year)+'&thisMonth='+ m
            req = urllib.request.Request(parse_url)
            req.add_header('User-agent', user_agent)
            page = urllib.request.urlopen(req).read()
            soup = BeautifulSoup(page, 'html.parser')
            print(parse_url)

            for ingredient in soup.find(id = "monthFd4").find_all('div', class_='slide'):
                name = str(ingredient.find('img'))
                name=name.split('alt=\"')[1].split("\"")[0]

                rows.append(tuple([name, month, 'plants']))
    print(rows)
    return rows

def connect_db() :
    conn= mysql.connector.connect(
        host = "localhost",
        user='root', password = '0000', database = 'eatwhat', auth_plugin='mysql_native_password'
    )
    return conn

def write_db(cursor, cols, values) :
    sql = "INSERT INTO seasonal_ingredients"
    for v in values :
        query = sql + cols +' values '+str(v)+';'
        cursor.execute(query)
        print(query)

rows = parse_seaonal('http://www.nongsaro.go.kr/portal/ps/psr/psrb/monthFdLst.ps?menuId=PS03924&code=251004')

conn = connect_db()
cursor = conn.cursor()
write_db(cursor,'(name, month, category)', rows)
conn.commit()
conn.close()
