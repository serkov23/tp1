from typing import List

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QPointF

from Figures.polygon import Polygon


class Rect(Polygon):
    def __init__(self, points: List[QPointF], color: QtGui.QColor = QtCore.Qt.black,
                 inner_color: QtGui.QColor = QtGui.QColor(QtCore.Qt.white)):
        super().__init__(points, color, inner_color)
        self.points = [points[0], QPointF(points[0].x(), points[1].y()), points[1],
                       QPointF(points[1].x(), points[0].y())]

    @staticmethod
    def points_needed() -> int:
        return 2