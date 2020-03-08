import math
from typing import List

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QPointF

from Figures.Figure import Figure
from Figures.polygon import Polygon


class RegularPolygon(Polygon):
    point_amm = Figure.UNDEFINED_POINTS

    def __init__(self, points: List[QPointF], color: QtGui.QColor = QtGui.QColor(QtCore.Qt.black),
                 inner_color: QtGui.QColor = QtGui.QColor(QtCore.Qt.transparent)):
        x = points[0].x() - points[1].x()
        y = points[0].y() - points[1].y()
        a = math.sqrt(x ** 2 + y ** 2)
        phi = math.pi if y == 0 else math.atan(x / y) + math.pi if y > 0 else 0
        dp = 2 * math.pi / self.point_amm
        li = [QPointF(points[0].x() + a * math.sin(phi + i * dp), points[0].y() + a * math.cos(phi + i * dp)) for i in
              range(self.point_amm)]
        RegularPolygon.point_amm = Figure.UNDEFINED_POINTS
        super().__init__(li, color, inner_color)

    @staticmethod
    def points_needed() -> int:
        return RegularPolygon.point_amm if RegularPolygon.point_amm == Figure.UNDEFINED_POINTS else 2
