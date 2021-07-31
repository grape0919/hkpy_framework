import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from view.main import Ui_MainWindow
from view.main import Ui_MainWindow

class WindowClass(QMainWindow, Ui_MainWindow) :

    def __init__(self) :
        super(WindowClass, self).__init__()

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()