from typing import List

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QPointF

from Figures.figure1D import Figure1D


class PolyLine(Figure1D):
    def __init__(self, points: List[QPointF], color: QtGui.QColor = QtGui.QColor(QtCore.Qt.black)):
        super().__init__(points, color)

    @staticmethod
    def points_needed() -> int:
        return PolyLine.UNLIMITED_POINTS

    def paint(self, scene: QtWidgets.QGraphicsScene):
        for i in range(1, len(self.points)):
            scene.addLine(QtCore.QLineF(self.points[i - 1], self.points[i]), self.color)
