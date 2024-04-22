import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic
form_class = uic.loadUiType("ui/member.ui")[0]  # 미리 제작해 놓은 ui 불러오기
class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원 관리 프로그램")
        self.join_btn.clicked.connect(self.member_join)  # 회원가입이 버튼이 클릭되면 가입함수 호출
        self.joinreset_btn.clicked.connect(self.join_reset)  # 초기화 버튼이 클릭되면 입력내용 초기화
        self.idcheck_btn.clicked.connect(self.idcheck)  # 회원가입여부 체크 버튼이 클릭되면 가입여부확인 함수 호출
        self.membersearch_btn.clicked.connect(self.member_search)  # 회원조회 버튼 클릭시 회원정보 출력
        self.memberreset_btn.clicked.connect(self.memberInfo_reset)  # 초기화 버튼 클릭되면 입력내용 초기화


    def member_join(self):  # 회원 가입 이벤트 처리 함수
        memberid = self.joinid_edit.text()  # 유저가 입력한 회원아이디 텍스트 가져오기
        memberpw = self.joinpw_edit.text()  # 유저가 입력한 회원비밀번호 텍스트 가져오기
        membername = self.joinname_edit.text()  # 유저가 입력한 회원이름 텍스트 가져오기
        memberemail = self.joinemail_edit.text()  # 유저가 입력한 회원이메일 텍스트 가져오기
        memberage = self.joinage_edit.text()  # 유저가 입력한 회원나이 텍스트 가져오기
        if memberid == "" or memberpw == "" or membername == "" or memberemail == "" or memberage == "":
            QMessageBox.warning(self, "정보입력오류", "입력 정보 중 한개라도 누락되면 회원가입이 되지 않습니다.\n다시 입력해주세요.")
        elif len(memberid) < 4 or len(memberid) >= 15:
            QMessageBox.warning(self, "아이디길이오류", "아이디는 4자 이상 14자 이하이어야 합니다.\n다시 입력해주세요.")
        elif len(memberpw) < 4 or len(memberpw) >= 15:
            QMessageBox.warning(self, "비밀번호길이오류", "비밀번호는 4자 이상 14자 이하이어야 합니다.\n다시 입력해주세요.")
        elif self.idcheck() == 0:  # 가입불가
            pass
        else:
            dbConn = pymysql.connect(user="root", password="12345", host="localhost", db="shopdb")
            sql = f"INSERT INTO appmember VALUES('{memberid}','{memberpw}','{membername}','{memberemail}','{memberage}')"
            cur = dbConn.cursor()
            result = cur.execute(sql)  # 회원가입하는 sql문이 성공하면 1이 반환
            if result == 1:
                QMessageBox.warning(self, "회원가입성공","축하합니다.\n회원가입이 성공하셨습니다.")
                self.join_reset()  # 회원가입 성공 ok 클릭 후 입력내용 초기화
            else:
                QMessageBox.warning(self, "회원가입실패", "회원가입이 실패하셨습니다.")
            cur.close()
            dbConn.commit()
            dbConn.close()
    def join_reset(self):  # 회원가입정보 입력내용 초기화
        self.joinid_edit.clear()
        self.joinpw_edit.clear()
        self.joinname_edit.clear()
        self.joinemail_edit.clear()
        self.joinage_edit.clear()
    def idcheck(self):  # 기존 아이디 회원가입여부 체크 함수
        memberid = self.joinid_edit.text()
        if memberid == "":
            QMessageBox.warning(self, "아이디입력오류", "아이디는 필수 입력사항입니다.\n아이디를 입력해주세요.")
        elif len(memberid) < 4 or len(memberid) >= 15:
            QMessageBox.warning(self, "아이디길이오류", "아이디는 4자 이상 14자 이하이어야 합니다.\n다시 입력해주세요.")
        else:
            dbConn = pymysql.connect(user="root", password="12345", host="localhost", db="shopdb")
            sql = f"SELECT count(*) FROM appmember WHERE memberid='{memberid}'"
            # SQL문 실행 시 1 또는 0이 반환(기존에 가입된 아이디면 1, 아니면 0)
            cur = dbConn.cursor()
            cur.execute(sql)  # 회원가입하는 sql문이 성공하면 1이 반환
            result = cur.fetchall()
            print(result)
            if result[0][0] == 1:
                QMessageBox.warning(self, "회원가입불가", "이미 가입된 아이디입니다.\n다시 입력해주세요.")
                return 0
            else:
                QMessageBox.warning(self, "회원가입가능", "가입 가능한 아이디입니다.\n계속해서 가입을 진행해주세요.")
                return 1
            cur.close()
            dbConn.close()

    def member_check(self):  # 회원가입여부 체크 함수
        memberid = self.memberid_edit.text()

        dbConn = pymysql.connect(user="root", password="12345", host="localhost", db="shopdb")

        sql = f"SELECT count(*) FROM appmember WHERE memberid='{memberid}'"
        # SQL문 실행 시 1 또는 0이 반환(기존에 가입된 아이디면 1, 아니면 0)

        cur = dbConn.cursor()
        cur.execute(sql)  # 회원가입하는 sql문이 성공하면 1이 반환
        result = cur.fetchall()

        print(result)

        if result[0][0] == 1:
            return 1
        else:
            QMessageBox.warning(self, "회원조회불가", "가입이 되지 않은 아이디입니다.\n다른 아이디를 입력해주세요.")
            return 0

            cur.close()
            dbConn.close()

    def member_search(self):  # 아이디로 회원을 조회하는 함수

        memberid = self.memberid_edit.text()  # 유저가 입력한 아이디 텍스트 가져오기
        dbConn = pymysql.connect(user="root", password="12345", host="localhost", db="shopdb")

        sql = f"SELECT * FROM appmember WHERE memberid='{memberid}'"
        # SQL문 실행 시 1 또는 0이 반환(기존에 가입된 아이디면 1, 아니면 0)

        if memberid == "":
            QMessageBox.warning(self, "아이디입력오류", "아이디는 필수 입력사항입니다.\n아이디를 입력해주세요.")
        elif self.member_check() == 0:
            pass
        else:
            cur = dbConn.cursor()
            cur.execute(sql)  # 회원가입하는 sql문이 성공하면 1이 반환
            result = cur.fetchall()

            print(result)

            self.memberpw_edit.setText(str(result[0][1]))  # 비밀번호 출력
            self.membername_edit.setText(str(result[0][2]))  # 회원이름 출력
            self.memberemail_edit.setText(str(result[0][3]))  # 이메일 출력
            self.memberage_edit.setText(str(result[0][4]))  # 회원나이 출력

    def memberInfo_reset(self):  # 회원조회정보 입력내용 초기화
        self.memberid_edit.clear()
        self.memberpw_edit.clear()
        self.membername_edit.clear()
        self.memberemail_edit.clear()
        self.memberage_edit.clear()



app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())