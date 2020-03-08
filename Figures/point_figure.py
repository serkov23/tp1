from typing import List

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QPointF

from Figures.Figure import Figure


class Point(Figure):
    def __init__(self, points: List[QPointF], color: QtGui.QColor = QtGui.QColor(QtCore.Qt.black)):
        super().__init__(points, color)

    @staticmethod
    def points_needed() -> int:
        return 1

    def x(self):
        return self.points[0].x()

    def y(self):
        return self.points[0].y()

    def paint(self, scene: QtWidgets.QGraphicsScene):
        scene.addEllipse(self.x(), self.y(), 1, 1, self.color, self.color)
