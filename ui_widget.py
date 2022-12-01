# -*- coding: utf-8 -*-
import random

################################################################################
## Form generated from reading UI file 'widgetlJxbcV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from paintFunctions import GraphSearch

from paint_widget import PaintWidget


class Ui_my_widget(QMainWindow):
    def __init__(self):
        super(Ui_my_widget, self).__init__()

        self.setupUi(self)
        self.retranslateUi(self)
        self.slot_init()

    def setupUi(self, my_widget):
        if not my_widget.objectName():
            my_widget.setObjectName(u"my_widget")
        my_widget.resize(685, 642)
        my_widget.setFixedSize(650, 650)
        self.paint_widget = PaintWidget()
        self.paint_widget.setParent(my_widget)
        self.paint_widget.setObjectName(u"paint_widget")
        self.checkBox_A = QCheckBox(self.paint_widget)
        self.checkBox_A.setObjectName(u"checkBox_17")
        self.checkBox_A.setGeometry(QRect(92, 488, 30, 20))
        self.checkBox_B = QCheckBox(self.paint_widget)
        self.checkBox_B.setObjectName(u"checkBox_3")
        self.checkBox_B.setGeometry(QRect(401, 323, 28, 20))
        self.checkBox_C = QCheckBox(self.paint_widget)
        self.checkBox_C.setObjectName(u"checkBox_4")
        self.checkBox_C.setGeometry(QRect(254, 284, 28, 20))
        self.checkBox_D = QCheckBox(self.paint_widget)
        self.checkBox_D.setObjectName(u"checkBox_9")
        self.checkBox_D.setGeometry(QRect(166, 295, 28, 20))
        self.checkBox_E = QCheckBox(self.paint_widget)
        self.checkBox_E.setObjectName(u"checkBox_2")
        self.checkBox_E.setGeometry(QRect(563, 289, 28, 20))
        self.checkBox_F = QCheckBox(self.paint_widget)
        self.checkBox_F.setObjectName(u"checkBox_13")
        self.checkBox_F.setGeometry(QRect(306, 445, 28, 20))
        self.checkBox_G = QCheckBox(self.paint_widget)
        self.checkBox_G.setObjectName(u"checkBox_10")
        self.checkBox_G.setGeometry(QRect(376, 266, 28, 20))
        self.checkBox_H = QCheckBox(self.paint_widget)
        self.checkBox_H.setObjectName(u"checkBox_8")
        self.checkBox_H.setGeometry(QRect(535, 346, 28, 20))
        self.checkBox_I = QCheckBox(self.paint_widget)
        self.checkBox_I.setObjectName(u"checkBox_6")
        self.checkBox_I.setGeometry(QRect(474, 502, 28, 20))

        self.checkBox_L = QCheckBox(self.paint_widget)
        self.checkBox_L.setObjectName(u"checkBox_12")
        self.checkBox_L.setGeometry(QRect(166, 375, 28, 20))
        self.checkBox_M = QCheckBox(self.paint_widget)
        self.checkBox_M.setObjectName(u"checkBox_7")
        self.checkBox_M.setGeometry(QRect(169, 335, 28, 20))
        self.checkBox_N = QCheckBox(self.paint_widget)
        self.checkBox_N.setObjectName(u"checkBox_16")
        self.checkBox_N.setGeometry(QRect(407, 533, 28, 20))
        self.checkBox_O = QCheckBox(self.paint_widget)
        self.checkBox_O.setObjectName(u"checkBox_15")
        self.checkBox_O.setGeometry(QRect(132, 567, 28, 20))
        self.checkBox_P = QCheckBox(self.paint_widget)
        self.checkBox_P.setObjectName(u"checkBox_5")
        self.checkBox_P.setGeometry(QRect(321, 364, 28, 20))
        self.checkBox_R = QCheckBox(self.paint_widget)
        self.checkBox_R.setObjectName(u"checkBox_14")
        self.checkBox_R.setGeometry(QRect(234, 406, 28, 20))
        self.checkBox_S = QCheckBox(self.paint_widget)
        self.checkBox_S.setObjectName(u"checkBox_11")
        self.checkBox_S.setGeometry(QRect(208, 453, 28, 20))
        self.checkBox_T = QCheckBox(self.paint_widget)
        self.checkBox_T.setObjectName(u"checkBox_20")
        self.checkBox_T.setGeometry(QRect(95, 406, 30, 20))
        self.checkBox_U = QCheckBox(self.paint_widget)
        self.checkBox_U.setObjectName(u"checkBox_19")
        self.checkBox_U.setGeometry(QRect(457, 346, 30, 20))
        self.checkBox_V = QCheckBox(self.paint_widget)
        self.checkBox_V.setObjectName(u"checkBox_18")
        self.checkBox_V.setGeometry(QRect(510, 440, 30, 20))
        self.checkBox_Z = QCheckBox(self.paint_widget)
        self.checkBox_Z.setObjectName(u"checkBox_21")
        self.checkBox_Z.setGeometry(QRect(109, 527, 30, 20))

        self.layoutWidget = QWidget(my_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(41, 6, 569, 231))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_deepth = QPushButton(self.layoutWidget)
        self.btn_deepth.setObjectName(u"btn_deepth")
        self.btn_deepth.setMinimumSize(QSize(40, 40))
        self.btn_deepth.setMaximumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.btn_deepth)

        self.btn_width = QPushButton(self.layoutWidget)
        self.btn_width.setObjectName(u"btn_width")
        self.btn_width.setMinimumSize(QSize(40, 40))
        self.btn_width.setMaximumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.btn_width)

        self.btn_greedy = QPushButton(self.layoutWidget)
        self.btn_greedy.setObjectName(u"btn_greedy")
        self.btn_greedy.setMinimumSize(QSize(40, 40))
        self.btn_greedy.setMaximumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.btn_greedy)

        self.btn_Astar = QPushButton(self.layoutWidget)
        self.btn_Astar.setObjectName(u"btn_Astar")
        self.btn_Astar.setMinimumSize(QSize(40, 40))
        self.btn_Astar.setMaximumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.btn_Astar)

        self.btn_clear = QPushButton(self.layoutWidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(40, 40))
        self.btn_clear.setMaximumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.btn_clear)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listView_3 = QTextBrowser(self.layoutWidget)
        self.listView_3.setObjectName(u"listView_3")

        self.horizontalLayout_2.addWidget(self.listView_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.listView_2 = QTextBrowser(self.layoutWidget)
        self.listView_2.setObjectName(u"listView_2")

        self.horizontalLayout_2.addWidget(self.listView_2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # 获取所有的checkbox
        self.list = self.paint_widget.findChildren(QCheckBox)
        # 计数器 保证每次只能两个
        self.count = 0

        self.retranslateUi(my_widget)

        QMetaObject.connectSlotsByName(my_widget)

    # setupUi

    def retranslateUi(self, my_widget):
        my_widget.setWindowTitle(QCoreApplication.translate("my_widget", u"罗马尼亚度假问题", None))
        self.checkBox_I.setText(QCoreApplication.translate("my_widget", u"I", None))
        self.checkBox_L.setText(QCoreApplication.translate("my_widget", u"L", None))
        self.checkBox_V.setText(QCoreApplication.translate("my_widget", u"V", None))
        self.checkBox_B.setText(QCoreApplication.translate("my_widget", u"B", None))
        self.checkBox_Z.setText(QCoreApplication.translate("my_widget", u"Z", None))
        self.checkBox_M.setText(QCoreApplication.translate("my_widget", u"M", None))
        self.checkBox_E.setText(QCoreApplication.translate("my_widget", u"E", None))
        self.checkBox_G.setText(QCoreApplication.translate("my_widget", u"G", None))
        self.checkBox_C.setText(QCoreApplication.translate("my_widget", u"C", None))
        self.checkBox_S.setText(QCoreApplication.translate("my_widget", u"S", None))
        self.checkBox_O.setText(QCoreApplication.translate("my_widget", u"O", None))
        self.checkBox_D.setText(QCoreApplication.translate("my_widget", u"D", None))
        self.checkBox_P.setText(QCoreApplication.translate("my_widget", u"P", None))
        self.btn_width.setText(QCoreApplication.translate("my_widget", u"\u5e7f\u5ea6\u4f18\u5148\u641c\u7d22", None))
        self.btn_deepth.setText(QCoreApplication.translate("my_widget", u"\u6df1\u5ea6\u4f18\u5148\u641c\u7d22", None))
        self.btn_greedy.setText(QCoreApplication.translate("my_widget", u"\u8d2a\u5a6a\u7b97\u6cd5", None))
        self.btn_Astar.setText(QCoreApplication.translate("my_widget", u"A*\u7b97\u6cd5", None))
        self.btn_clear.setText(QCoreApplication.translate("my_widget", u"\u6e05\u9664", None))
        self.checkBox_N.setText(QCoreApplication.translate("my_widget", u"N", None))
        self.checkBox_F.setText(QCoreApplication.translate("my_widget", u"F", None))
        self.checkBox_A.setText(QCoreApplication.translate("my_widget", u"A", None))
        self.checkBox_H.setText(QCoreApplication.translate("my_widget", u"H", None))
        self.checkBox_T.setText(QCoreApplication.translate("my_widget", u"T", None))
        self.checkBox_R.setText(QCoreApplication.translate("my_widget", u"R", None))
        self.checkBox_U.setText(QCoreApplication.translate("my_widget", u"U", None))

    def slot_init(self):
        # 绑定事件
        self.btn_width.clicked.connect(lambda: self.BFS())
        self.btn_deepth.clicked.connect(lambda: self.DFS())
        self.btn_greedy.clicked.connect(lambda: self.greedySearch())
        self.btn_Astar.clicked.connect(lambda: self.AstarSearch())
        self.btn_clear.clicked.connect(lambda: self.clearAll())
        for i in self.list:
            i.clicked.connect(lambda: self.checkBtn())

    def BFS(self):
        # self.findStartAndEnd()
        if self.paint_widget.start == "" or self.paint_widget.end == "":
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '请先选择起点和终点！')
            msg_box.exec_()
            return
        self.paint_widget.gs = GraphSearch(self.paint_widget.start,
                                           self.paint_widget.end)  # 第一个参数是起点城市名的首字母 第二个是终点城市名的首字母
        self.paint_widget.gs.constructGraph()  # 构建城市图
        self.paint_widget.graph = self.paint_widget.gs.graph
        self.paint_widget.gs.widthFirstSearch()

        self.paint_widget.type = 0
        self.paint_widget.update()
        self.printPath(self.paint_widget.gs.close_width)
        pass

    def DFS(self):
        # self.findStartAndEnd()
        if self.paint_widget.start == "" or self.paint_widget.end == "":
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '请先选择起点和终点！')
            msg_box.exec_()
            return
        self.paint_widget.gs = GraphSearch(self.paint_widget.start,
                                           self.paint_widget.end)  # 第一个参数是起点城市名的首字母 第二个是终点城市名的首字母
        self.paint_widget.gs.constructGraph()  # 构建城市图
        self.paint_widget.graph = self.paint_widget.gs.graph
        self.paint_widget.gs.deepFirstSearch()
        self.paint_widget.type = 1
        self.paint_widget.update()
        self.printPath(self.paint_widget.gs.close_deepth)
        pass

    def greedySearch(self):
        if self.paint_widget.start == "" or self.paint_widget.end == "":
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '请先选择起点和终点！')
            msg_box.exec_()
            return
        # self.findStartAndEnd()
        self.paint_widget.gs = GraphSearch(self.paint_widget.start,
                                           self.paint_widget.end)  # 第一个参数是起点城市名的首字母 第二个是终点城市名的首字母
        self.paint_widget.gs.constructGraph()  # 构建城市图
        self.paint_widget.graph = self.paint_widget.gs.graph
        self.paint_widget.gs.greedSearch()
        self.paint_widget.type = 2
        self.paint_widget.update()
        self.printPath(self.paint_widget.gs.close_greed)
        pass

    def AstarSearch(self):
        if self.paint_widget.start == "" or self.paint_widget.end == "":
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '请先选择起点和终点！')
            msg_box.exec_()
            return
        self.paint_widget.gs = GraphSearch(self.paint_widget.start,
                                           self.paint_widget.end)  # 第一个参数是起点城市名的首字母 第二个是终点城市名的首字母
        self.paint_widget.gs.constructGraph()  # 构建城市图
        self.paint_widget.graph = self.paint_widget.gs.graph
        self.paint_widget.gs.AstarAlgorithm()
        self.paint_widget.type = 3
        self.paint_widget.update()
        self.printPath(self.paint_widget.gs.close_Astar)

        pass

    def clearAll(self):
        self.paint_widget.type = -1
        self.paint_widget.update()
        self.listView_2.setText("")
        self.listView_3.setText("")
        self.count = 0
        for i in self.list:
            i.setChecked(False)
        pass

    def checkBtn(self):
        for i in self.list:
            if i.isChecked():
                if i.text() != self.paint_widget.start:
                    if self.count == 0:
                        self.paint_widget.start = i.text()
                    self.count += 1

                if i.text() != self.paint_widget.start and self.count == 2:
                    self.paint_widget.end = i.text()

        if self.count > 2:
            self.count = 0
            for i in self.list:
                i.setChecked(False)

            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '您选择的点太多！')
            msg_box.exec_()
            self.clearAll()
            return

    # def findStartAndEnd(self):
    #     count = 0
    #     for i in self.list:
    #         if i.isChecked():
    #             if count == 0:
    #                 self.paint_widget.start = i.text()
    #                 count = 1
    #
    #                 continue
    #             elif count == 1:
    #                 self.paint_widget.end = i.text()

    def printPath(self, close):
        endNode = close[-1]
        path = [endNode.name]
        # 从终点向前找
        while path[-1] != self.paint_widget.gs.start:
            if endNode.prev:
                path.append(endNode.prev.name)
                endNode = endNode.prev
        path.reverse()
        self.listView_2.setText("搜索路径：" + str(path))
        close1 = []
        for i in close:
            close1.append(i.name)
        self.listView_3.setText("close表：" + str(close1))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = Ui_my_widget()
    ui.show()
    sys.exit(app.exec_())
