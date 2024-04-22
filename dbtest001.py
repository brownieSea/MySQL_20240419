import pymysql

# 1) 계정 : root(관리자 계정)
# 2) 비밀번호 : 12345
# 3) 데이터베이스가 설치된 컴퓨터의 ip 주소
#   - 본인 컴퓨터면 localhost, 다른 컴퓨터면 그 컴퓨터의 ip 주소
#   - 192.168.0.100 (교수용 컴퓨터 ip). port:3306
# 4) 데이터베이스 스키마 이름(ex:shopdb)

dbConn = pymysql.connect(host='localhost', user='root', password='12345', db='shopdb')
# 파이썬과 mysql간의 conncection 생성

sql = "SELECT * FROM membertbl"  # DB에 실행할 SQL문 생성

cur = dbConn.cursor()
cur.execute(sql) # 연결된 DB의 스키마에 지정된 SQL 문이 실행됨


records = cur.fetchall() # sql문에서 실행된 select문의 결과를 records로 받음 (튜플로 반환)

print(records)
print(records[0])  # 특정 레코드(1행)
print(records[0][1]) # 특ㅈㅇ 레코드의 특정 값(ex:이순신)

for member in records:
    print(member)  # 레코드 단위로 출력
    print(member[0])  # 아이디만 추출하여 출력

# dbConn의 사용이 종료된 후에는 반드시 닫아줄 것 (close:cur 먼저 닥고 dbConn을 닫아야 함)
cur.close()
doConn.close()