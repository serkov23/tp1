from typing import List

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QPointF

from Figures.Figure import Figure
from Figures.Figure2D import Figure2D


class Polygon(Figure2D):
    def __init__(self, points: List[QPointF], color: QtGui.QColor = QtGui.QColor(QtCore.Qt.black),
                 inner_color: QtGui.QColor = QtGui.QColor(QtCore.Qt.transparent)):
        super().__init__(points, color, inner_color)


    @staticmethod
    def points_needed() -> int:
        return Figure.UNLIMITED_POINTS

    def paint(self, scene: QtWidgets.QGraphicsScene):
        poly = QtGui.QPolygonF(self.points)
        scene.addPolygon(poly, self.color, self.inner_color)