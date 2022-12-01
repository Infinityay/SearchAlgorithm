from collections import deque

from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter, QPen
from PySide2.QtWidgets import QWidget
from paintFunctions import GraphSearch


class PaintWidget(QWidget):
    def __init__(self):
        super(PaintWidget, self).__init__()
        self.resize(600, 800)  # 设置主窗口尺寸

        # 默认不画
        self.type = -1
        # 默认起点和终点分别是是 A 和 B
        self.start = ''
        self.end = ''

        self.cities = GraphSearch(self.start, self.end).cities

        # self.gs = GraphSearch(self.start, self.end)  # 第一个参数是起点城市名的首字母 第二个是终点城市名的首字母
        # self.gs.constructGraph()  # 构建城市图
        # self.graph = self.gs.graph
        # self.gs.widthFirstSearch()
        # self.gs.deepFirstSearch()
        # self.gs.greedSearch()
        # self.gs.AstarAlgorithm()

    def paintEvent(self, event):
        painter = QPainter(self)  # 创建对象
        painter.begin(self)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(Qt.gray)
        painter.setPen(pen)
        # 默认用灰色 3宽度画
        self.connectAllCities(painter)

        self.drawAlogrithm(painter, self.type)

        painter.end()

    def connectAllCities(self, painter):
        for i in self.cities.keys():
            point1 = self.cities[i][0]
            for j in self.cities[i][1]:
                point2_name = j[0]
                point2 = self.cities[point2_name][0]
                painter.drawLine(point1[0], point1[1], point2[0], point2[1])

                distance = str(j[1])
                painter.drawText((point1[0] + point2[0]) // 2 + 7, (point1[1] + point2[1]) // 2 + 7, distance)

    def drawAlogrithm(self, painter, type):
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(Qt.red)
        painter.setPen(pen)
        if type == 0:
            close = self.gs.close_width
        elif type == 1:
            close = self.gs.close_deepth
        elif type == 2:
            close = self.gs.close_greed
        elif type == 3:
            close = self.gs.close_Astar
        else:
            return
        # 画所有close表的前驱节点的连线
        for i in reversed(close):
            endNode = i
            while endNode.prev:
                painter.drawLine(endNode.prev.point[0], endNode.prev.point[1], endNode.point[0], endNode.point[1])
                endNode = endNode.prev
        # 画最终选择的线路
        endNode = close[-1]
        pen.setWidth(1)
        pen.setColor(Qt.green)
        painter.setPen(pen)
        while endNode.prev:
            painter.drawLine(endNode.prev.point[0], endNode.prev.point[1], endNode.point[0], endNode.point[1])
            endNode = endNode.prev
