from typing import List

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QPointF, QRectF

from Figures.Figure2D import Figure2D


class Ellipse(Figure2D):
    def __init__(self, points: List[QPointF], color: QtGui.QColor = QtGui.QColor(QtCore.Qt.black),
                 inner_color: QtGui.QColor = QtGui.QColor(QtCore.Qt.white)):
        super().__init__(points, color, inner_color)

    def paint(self, scene: QtWidgets.QGraphicsScene):
        scene.addEllipse(QRectF(self.points[0], self.points[1]), self.color, self.inner_color)

    @staticmethod
    def points_needed() -> int:
        return 2
