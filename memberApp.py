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


    def member_join(self):  # 회원 가입 이벤트 처리 함수
        memberid = self.joinid_edit.text()  # 유저가 입력한 회원아이디 텍스트 가져오기
        memberpw = self.joinpw_edit.text()  # 유저가 입력한 회원비밀번호 텍스트 가져오기
        membername = self.joinname_edit.text()  # 유저가 입력한 회원이름 텍스트 가져오기
        memberemail = self.joinemail_edit.text()  # 유저가 입력한 회원이메일 텍스트 가져오기
        memberage = self.joinage_edit.text()  # 유저가 입력한 회원나이 텍스트 가져오기

        dbConn = pymysql.connect(user="root", password="12345", host="localhost", db="shopdb")

        sql = f"INSERT INTO appmember VALUES('{memberid}','{memberpw}','{membername}','{memberemail}','{memberage}')"

        cur = dbConn.cursor()
        result = cur.execute(sql)  # 회원가입하는 sql문이 성공하면 1이 반환

        cur.close()
        dbConn.commit()
        dbConn.close()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())