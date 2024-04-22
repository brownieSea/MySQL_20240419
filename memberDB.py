import pymysql

dbConn = pymysql.connect(user='root', password='12345', host='localhost', db='shopdb')

while True:
    print("======== 회원관리 프로그램 =========")
    print("1 : 회원 가입")
    print("2 : 회원 정보 변경")
    print("3 : 회원 탈퇴")
    print("4 : 전체 회원목록 조회")
    print("5 : 프로그램 종료")
    print("=================================")
    menuNum = input("메뉴 중 한가지를 선택하세요(1~5) : ")

    if menuNum == "1":
        print("회원 정보를 입력하세요")
        memberID = input("아이디 : ")
        memberName = input("이름 : ")
        address = input("주소 : ")
        sql = f"INSERT INTO membertbl VALUES ('{memberID}', '{memberName}', '{address}')"
        cur = dbConn.cursor()
        result = cur.execute(sql)
        if result == 1:
            print("회원가입 성공")
        else:
            print("회원가입 실패")

        cur.close()
        dbConn.commit()

    elif menuNum == "2":
        print("수정할 정보를 입력하세요")
        memberID = input("아이디 : ")
        memberName = input("이름 : ")
        address = input("주소 : ")
        sql = f"UPDATE membertbl SET memberName='{memberName}', memberAddress='{address}' WHERE memberId = '{memberID}'"
        cur = dbConn.cursor()
        result = cur.execute(sql)
        if result == 1:
            print("정보 변경 성공")
        else:
            print("정보 변경 실패")

        cur.close()
        dbConn.commit()

    elif menuNum == "3":
        print("탈퇴할 아이디를 입력하세요")
        memberID = input("아이디 : ")
        sql = f"DELETE FROM membertbl WHERE memberId = '{memberID}'"
        cur = dbConn.cursor()
        result = cur.execute(sql)
        if result == 1:
            print("회원 탈퇴 성공")
        else:
            print("회원 탈퇴 실패")

        cur.close()
        dbConn.commit()

    elif menuNum == "4":
        print("조회하신 전체 회원 정보입니다.")
        sql = f"SELECT * FROM membertbl"
        cur = dbConn.cursor()
        result = cur.execute(sql)
        memberList = cur.fetchall()  # select 문의 결과를 받아온다 (튜플)
        # record_count = cur.rowcount

        i = 0
        for member in memberList:
            i += 1
            print(f"{i} : {member[0]} / {member[1]} / {member[2]}")

        if result > 0:
            print(f"{i} 건의 회원 정보를 조회 완료했습니다.")
        else:
            print("회원 정보 조회를 실패했습니다.")

        cur.close()
        dbConn.commit()

    elif menuNum == "5":
        print("프로그램을 종료합니다.")
        dbConn.close()
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
