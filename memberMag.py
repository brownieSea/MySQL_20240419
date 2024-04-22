import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic
form_class = uic.loadUiType('ui/member.ui')[0]
class MainWindow(QMainWindow, form_class):
    # 초기화자
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원 관리 프로그램")
        self.join_btn.clicked.connect(self.member_join)  # 회원가입 버튼을 클릭하면 회원가입 함수(member_join) 호출
        self.joinreset_btn.clicked.connect(self.join_reset)  # 초기화 버튼을 클릭하면 입력 내용 초기화
        self.idcheck_btn.clicked.connect(self.idcheck)
        self.membersearch_btn.clicked.connect(self.member_search)
        self.memberreset_btn.clicked.connect(self.memberinfo_reset)  # 초기화 버튼을 클릭하면 입력 내용 초기화
        self.membermodify_btn.clicked.connect(self.member_modify)  # 회원정보 수정 함수 호출
        self.login_btn.clicked.connect(self.member_login)  # 회원정보 수정 함수 호출
        self.loginreset_btn.clicked.connect(self.login_reset)  # 초기화 버튼을 클릭하면 입력 내용 초기화
        self.exit_btn.clicked.connect(self.member_exit)  # 회원정보 수정 함수 호출

    def member_join(self):  # 회원가입 이벤트 처리 함수
        memberid = self.joinid_edit.text()  # user가 입력한 회원 ID text를 가져온다
        memberpw = self.joinpw_edit.text()  # 비밀번호.text
        membername = self.joinname_edit.text()  # 이름.text
        membermail = self.joinemail_edit.text()  # 이메일.text
        memberage = self.joinage_edit.text()  # 나이.text
        if memberid == "" or memberpw == "" or membername == "" or membermail == "" or memberage =="":
            QMessageBox.warning(self, "오류 발생", "입력 정보가 누락되었습니다.\n다시 입력해 주세요")
        elif len(memberid) < 4 or len(memberid) > 15:
            QMessageBox.warning(self, "오류 발생", "아이디는 4자 이상 14자 이하이어야 합니다.\n다시 입력해주세요")
        elif len(memberpw) < 4 or len(memberpw) > 15:
            QMessageBox.warning(self, "오류 발생", "비밀번호는 4자 이상 14자 이하이어야 합니다.\n다시 입력해주세요")
        elif self.idcheck() == 0:  # 가입불가
            pass
        else:
            dbConn = pymysql.connect(user='root', password='12345', host='localhost', db='shopdb')
            sql = f"INSERT INTO appmember VALUES ('{memberid}', '{memberpw}', '{membername}', '{membermail}', '{memberage}')"
            cur = dbConn.cursor()
            result = cur.execute(sql)  # 회원 가입하는 sql 문이 성공하면 1 반환
            if result == 1:
                QMessageBox.warning(self, "회원가입 성공", "회원가입이 완료되었습니다.")
                self.join_reset()  # 회원가입 성공 후 Ok 클릭하게 되면 입력 내용 초기화
            else:
                QMessageBox.warning(self, "회원가입 실패", "회원가입에 실패했습니다.")
            cur.close()
            dbConn.commit()
            dbConn.close()
    def join_reset(self):   # 회원가입 정보 초기화
        self.joinid_edit.clear()  # user가 입력한 회원 ID text를 가져온다
        self.joinpw_edit.clear()  # 비밀번호.text
        self.joinname_edit.clear()  # 이름.text
        self.joinemail_edit.clear()  # 이메일.text
        self.joinage_edit.clear()  # 나이.text
    def idcheck(self): # 아이디 중복 체크 함수
        memberid = self.joinid_edit.text()  # user가 입력한 회원 ID text를 가져온다
        if memberid == "":
            QMessageBox.warning(self, "오류 발생", "아이디는 필수 입력 사항입니다.\n다시 입력해 주세요")
        elif len(memberid) < 4 or len(memberid) > 15:
            QMessageBox.warning(self, "오류 발생", "아이디는 4자 이상 14자 이하이어야 합니다.\n다시 입력해주세요")
        else:
            dbConn = pymysql.connect(user='root', password='12345', host='localhost', db='shopdb')
            sql = f"SELECT count(*) FROM appmember WHERE memberid = '{memberid}'"
            # sql문 실행시 1 또는 0이 반환 (기존에 가입된 아이디면 1, 아니면 0
            cur = dbConn.cursor()
            cur.execute(sql)
            result = cur.fetchall()  # 조건에 맞는 데이터가 있으면 1 반환 (튜를로 반환)
            print(result)
            if result[0][0] == 1:  # 튜플 값이 1이면
                QMessageBox.warning(self, "오류 발생", "이미 사용중인 아이디입니다.\n다시 입력해 주세요")
                return 0  # 중복이면 0을 반환
            else:
                QMessageBox.warning(self, "회원가입 가능", "사용 가능한 아이디입니다.")
                return 1  # 중복이 아니면 1을 반환

            cur.close()
            dbConn.close()

    def membercheck(self): # 아이디 중복 체크 함수
        memberid = self.memberid_edit.text()  # user가 입력한 회원 ID text를 가져온다

        dbConn = pymysql.connect(user='root', password='12345', host='localhost', db='shopdb')

        sql = f"SELECT count(*) FROM appmember WHERE memberid = '{memberid}'"
        # sql문 실행시 1 또는 0이 반환 (기존에 가입된 아이디면 1, 아니면 0

        cur = dbConn.cursor()
        cur.execute(sql)
        result = cur.fetchall()

        print(result)

        if result[0][0] == 1:  # 튜플 값이 1이면
            return 1  # 회원 정보 조회가 가능
        else:
            QMessageBox.warning(self, "오류 발생", "가입되어 있지 않은 아이디입니다.\n아이디를 다시 입력해주세요")
            return 0

        cur.close()
        dbConn.close()

    def member_search(self):
        memberid = self.memberid_edit.text()  # user가 입력한 회원 ID text를 가져온다
        dbConn = pymysql.connect(user='root', password='12345', host='localhost', db='shopdb')

        sql = f"SELECT * FROM appmember WHERE memberid = '{memberid}'"

        if memberid == "":
            QMessageBox.warning(self, "오류 발생", "아이디를 입력해야 조회가 가능합니다.\n아이디를 입력해주세요")
        elif self.membercheck() == 0:
            pass
        else:
            cur = dbConn.cursor()
            cur.execute(sql)
            result = cur.fetchall()
            print(result)

            self.memberpw_edit.setText(str(result[0][1]))
            self.membername_edit.setText(str(result[0][2]))
            self.memberemail_edit.setText(str(result[0][3]))
            self.memberage_edit.setText(str(result[0][4]))
    def memberinfo_reset(self):   # 회원가입 정보 초기화
        self.memberid_edit.clear()  # user가 입력한 회원 ID text를 가져온다
        self.memberpw_edit.clear()  # 비밀번호.text
        self.membername_edit.clear()  # 이름.text
        self.memberemail_edit.clear()  # 이메일.text
        self.memberage_edit.clear()  # 나이.text
    def member_modify(self):  # 회원정보 수정 함수
        memberid = self.memberid_edit.text()  # ID.text
        memberpw = self.memberpw_edit.text()  # 비밀번호.text
        membername = self.membername_edit.text()  # 이름.text
        memberemail = self.memberemail_edit.text()  # 이메일.text
        memberage = self.memberage_edit.text()  # 나이.text

        dbConn = pymysql.connect(user='root', password='12345', host='localhost', db='shopdb')
        sql = f"UPDATE appmember SET memberPW='{memberpw}', memberName='{membername}', memberEmail='{memberemail}', memberAge='{memberage}' WHERE memberID='{memberid}'"
        cur = dbConn.cursor()
        result = cur.execute(sql)  # 회원 가입하는 sql 문이 성공하면 1 반환
        if result == 1:
            QMessageBox.warning(self, "성공", "회원 정보가 수정되었습니다.")
        else:
            QMessageBox.warning(self, "실패", "회원 정보 갱신에 실패했습니다.")

        cur.close()
        dbConn.commit()
        dbConn.close()

    def member_login(self):
        loginid = self.loginid_edit.text()  # ID.text
        loginpw = self.loginpw_edit.text()  # 비밀번호.text

        if loginid == "" or loginpw == "":
            QMessageBox.warning(self, "오류 발생", "아이디 또는 비밀번호를 반드시 입력하세요.")
        else:
            dbConn = pymysql.connect(user='root', password='12345', host='localhost', db='shopdb')
            sql = f"SELECT count(*) FROM appmember WHERE memberID='{loginid}' AND memberPW = '{loginpw}'"
            # 아이디와 비밀번호가 모두 일치하는 레코드의 갯수를 반환 (1 혹은 0)

            cur = dbConn.cursor()
            cur.execute(sql)
            result = cur.fetchall()

            if result[0][0] == 1:
                self.loginid_edit.clear()  # user가 입력한 회원 ID text를 가져온다
                self.loginpw_edit.clear()  # 비밀번호.text
                QMessageBox.warning(self, "성공", "로그인 완료")
            else:
                QMessageBox.warning(self, "오류 발생", "아이디나 비밀번호 정보가 맞지 않습니다.\n다시 입력해주세요")

    def login_reset(self):   # 회원가입 정보 초기화
        self.loginid_edit.clear()  # user가 입력한 회원 ID text를 가져온다
        self.loginpw_edit.clear()  # 비밀번호.text


    def member_exit(self):
        exitid = self.memberid_exit.text()  # ID.text
        exitpw = self.memberpw_exit.text()  # 비밀번호.text

        if exitid == "" or exitpw == "":
            QMessageBox.warning(self, "오류 발생", "아이디와 비밀번호를 반드시 입력하세요.")
        else:
            dbConn = pymysql.connect(user='root', password='12345', host='localhost', db='shopdb')
            sql = f"DELETE FROM appmember WHERE memberID='{exitid}' AND memberPW = '{exitpw}'"
            # 아이디와 비밀번호가 모두 일치하는 레코드의 갯수를 반환 (1 혹은 0)

            cur = dbConn.cursor()
            result = cur.execute(sql)
            print(result)
            if result == 1:
                self.memberid_exit.clear()  # user가 입력한 회원 ID text를 가져온다
                self.memberpw_exit.clear()  # 비밀번호.text
                QMessageBox.warning(self, "성공", "회원정보가 삭제되었습니다.")
            else:
                QMessageBox.warning(self, "오류 발생", "아이디나 비밀번호 정보가 맞지 않습니다.\n다시 입력해주세요")

            cur.close()
            dbConn.commit()
            dbConn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())