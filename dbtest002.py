import pymysql

# 1) 계정 : root(관리자 계정)
# 2) 비밀번호 : 12345
# 3) 데이터베이스가 설치된 컴퓨터의 ip 주소
#   - 본인 컴퓨터면 localhost, 다른 컴퓨터면 그 컴퓨터의 ip 주소
#   - 192.168.0.100 (교수용 컴퓨터 ip)
# 4) 데이터베이스 스키마 이름(ex:shopdb)

dbConn = pymysql.connect(host='localhost', user='root', password='12345', db='shopdb')
# 파이썬과 mysql간의 conncection 생성

sql = "INSERT INTO membertbl VALUES ('WhiteCat3',  '임양고', '강원도 양양군')"
# DB에 실행할 SQL문 생성

cur = dbConn.cursor()
result = cur.execute(sql) # 연결된 DB의 스키마에 지정된 SQL 문이 실행됨

# Insert, update, delete 문이 실행된 후 성공결과를 반환해 줌 --> 1이면 성공
if result == 1:
    print("회원 가입이 성공하였습니다.")



# dbConn의 사용이 종료된 후에는 반드시 닫아줄 것 (close:cur 먼저 닥고 dbConn을 닫아야 함)
cur.close()
dbConn.commit() # insert, delete, update 문을 사용한 경우에는 반드시 commit 함수를 호출해야함!
dbConn.close()