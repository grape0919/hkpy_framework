from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont

buttonSize = QSize(100,40)

#버튼 폰트
buttonFont = QFont()
buttonFont.setBold(True)
#버튼 styleSheet
buttonStyleSheet = "color: white;"
buttonStyleSheet += "background-color: #2F92FA;"
buttonStyleSheet += "border-style: solid;"
buttonStyleSheet += "border-width: 2px;"
buttonStyleSheet += "border-color: #2F92FA;"
buttonStyleSheet += "border-radius: 5px"


#disabled styleSheet
disabledStyleSheet = "color: #838383;"

#enabled styleSheet
enabledStyleSheet = "color: #000000;"

        # #메인 화면 색상py
        # self.setStyleSheet("color: black;"
        #                 "background-color: white")

        #  #버튼 스타일 변경
        # self.button_activate.setStyleSheet(staticValues.buttonStyleSheet)
        # self.button_activate.setFont(staticValues.buttonFont)