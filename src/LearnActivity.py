from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
import sys
import PyQt5


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi('UI_Files/learn_activity.ui', self)

        """ 현재 모드를 나타냄 ( 모든 로직은 이 변수를 이용해서 처리 ex. mode = A -> 튜토리얼 사진 show 'A' """
        self.currentMode = 'A'
        """ OnFirstRun """
        self.notifyModeChanged(self.currentMode)

        # label의 값을 조정하기위해서는 데이터 타입을 PyQt5.QtCore.QSize로 넘겨줘야 됨.
        # movie.setScaledSize(s) # PyQt5.QtCore.QSize(360, 270)로 넘겨줘도 됨.
        # self.label_3.setGeometry(0, 0, 780, 441) 아니면 이거 사용해도될듯.. 늦게 서야 봄..
        # movie.setScaledSize(PyQt5.QtCore.QSize(360,270))

        # self.label_imageView.setMovie(movie)
        # movie.start()

        # self.button_A = PicButton(QPixmap("./resource/alphabet/learn/A.png"))
        self.button_A.setIcon(QtGui.QIcon("./resource/alphabet/button/A.png"))
        self.button_A.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(self.alphabetButtonClicked)

        self.button_B.setIcon(QtGui.QIcon("./resource/alphabet/button/B.png"))
        self.button_B.setIconSize(QSize(30, 30))
        self.button_B.clicked.connect(self.alphabetButtonClicked)

        self.button_C.setIcon(QtGui.QIcon("./resource/alphabet/button/C.png"))
        self.button_C.setIconSize(QSize(30, 30))
        self.button_C.clicked.connect(self.alphabetButtonClicked)

        self.button_D.setIcon(QtGui.QIcon("./resource/alphabet/button/D.png"))
        self.button_D.setIconSize(QSize(30, 30))
        self.button_D.clicked.connect(self.alphabetButtonClicked)

        self.button_E.setIcon(QtGui.QIcon("./resource/alphabet/button/E.png"))
        self.button_E.setIconSize(QSize(30, 30))
        self.button_E.clicked.connect(self.alphabetButtonClicked)

        self.button_F.setIcon(QtGui.QIcon("./resource/alphabet/button/F.png"))
        self.button_F.setIconSize(QSize(30, 30))
        self.button_F.clicked.connect(self.alphabetButtonClicked)

        self.button_G.setIcon(QtGui.QIcon("./resource/alphabet/button/G.png"))
        self.button_G.setIconSize(QSize(30, 30))
        self.button_G.clicked.connect(self.alphabetButtonClicked)

        self.button_H.setIcon(QtGui.QIcon("./resource/alphabet/button/H.png"))
        self.button_H.setIconSize(QSize(30, 30))
        self.button_H.clicked.connect(self.alphabetButtonClicked)

        self.button_I.setIcon(QtGui.QIcon("./resource/alphabet/button/I.png"))
        self.button_I.setIconSize(QSize(30, 30))
        self.button_I.clicked.connect(self.alphabetButtonClicked)

        self.button_J.setIcon(QtGui.QIcon("./resource/alphabet/button/J.png"))
        self.button_J.setIconSize(QSize(30, 30))
        self.button_J.clicked.connect(self.alphabetButtonClicked)

        self.button_K.setIcon(QtGui.QIcon("./resource/alphabet/button/K.png"))
        self.button_K.setIconSize(QSize(30, 30))
        self.button_K.clicked.connect(self.alphabetButtonClicked)

        self.button_L.setIcon(QtGui.QIcon("./resource/alphabet/button/L.png"))
        self.button_L.setIconSize(QSize(30, 30))
        self.button_L.clicked.connect(self.alphabetButtonClicked)

        self.button_M.setIcon(QtGui.QIcon("./resource/alphabet/button/M.png"))
        self.button_M.setIconSize(QSize(30, 30))
        self.button_M.clicked.connect(self.alphabetButtonClicked)

        self.button_N.setIcon(QtGui.QIcon("./resource/alphabet/button/N.png"))
        self.button_N.setIconSize(QSize(30, 30))
        self.button_N.clicked.connect(self.alphabetButtonClicked)

        self.button_O.setIcon(QtGui.QIcon("./resource/alphabet/button/O.png"))
        self.button_O.setIconSize(QSize(30, 30))
        self.button_O.clicked.connect(self.alphabetButtonClicked)

        self.button_P.setIcon(QtGui.QIcon("./resource/alphabet/button/P.png"))
        self.button_P.setIconSize(QSize(30, 30))
        self.button_P.clicked.connect(self.alphabetButtonClicked)

        self.button_Q.setIcon(QtGui.QIcon("./resource/alphabet/button/Q.png"))
        self.button_Q.setIconSize(QSize(30, 30))
        self.button_Q.clicked.connect(self.alphabetButtonClicked)

        self.button_R.setIcon(QtGui.QIcon("./resource/alphabet/button/R.png"))
        self.button_R.setIconSize(QSize(30, 30))
        self.button_R.clicked.connect(self.alphabetButtonClicked)

        self.button_S.setIcon(QtGui.QIcon("./resource/alphabet/button/S.png"))
        self.button_S.setIconSize(QSize(30, 30))
        self.button_S.clicked.connect(self.alphabetButtonClicked)

        self.button_T.setIcon(QtGui.QIcon("./resource/alphabet/button/T.png"))
        self.button_T.setIconSize(QSize(30, 30))
        self.button_T.clicked.connect(self.alphabetButtonClicked)

        self.button_U.setIcon(QtGui.QIcon("./resource/alphabet/button/U.png"))
        self.button_U.setIconSize(QSize(30, 30))
        self.button_U.clicked.connect(self.alphabetButtonClicked)

        self.button_V.setIcon(QtGui.QIcon("./resource/alphabet/button/V.png"))
        self.button_V.setIconSize(QSize(30, 30))
        self.button_V.clicked.connect(self.alphabetButtonClicked)

        self.button_W.setIcon(QtGui.QIcon("./resource/alphabet/button/W.png"))
        self.button_W.setIconSize(QSize(30, 30))
        self.button_W.clicked.connect(self.alphabetButtonClicked)

        self.button_X.setIcon(QtGui.QIcon("./resource/alphabet/button/X.png"))
        self.button_X.setIconSize(QSize(30, 30))
        self.button_X.clicked.connect(self.alphabetButtonClicked)

        self.button_Y.setIcon(QtGui.QIcon("./resource/alphabet/button/Y.png"))
        self.button_Y.setIconSize(QSize(30, 30))
        self.button_Y.clicked.connect(self.alphabetButtonClicked)

        self.button_Z.setIcon(QtGui.QIcon("./resource/alphabet/button/Z.png"))
        self.button_Z.setIconSize(QSize(30, 30))
        self.button_Z.clicked.connect(self.alphabetButtonClicked)

        # self.pushButton.setGeometry(0,0,300,300)
        # self.widget.setIcon("./resource/alphabet/learn/A.png")

        # QtGui.QIcon
        # print(self.widget)
        # print(type(self.widget))

    def alphabetButtonClicked(self):
        button = self.sender()

        objName = button.objectName()
        # Convert 'button_A' -> 'A'
        self.notifyModeChanged(objName[-1])

    """ 뷰 내의 모든 위젯은 이 함수를 호출해 Refresh 함 """
    def notifyModeChanged(self, modeName):
        self.currentMode = modeName
        self.loadTutorialImageFromMode()
        print('Mode Changed To {}'.format(self.currentMode))

    """ label_tutorialView 에 현재 모드에 맞는 튜토리얼 이미지 삽입 """
    def loadTutorialImageFromMode(self):
        image = QPixmap("./resource/alphabet/learn/{}.png".format(self.currentMode))
        image = image.scaled(300, 190)
        self.label_tutorialView.setPixmap(image)


app = QApplication([])
window = MainWindow()
window.show()

app.exec_()
