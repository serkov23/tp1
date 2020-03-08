from typing import List

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QPointF

from Figures.figure1D import Figure1D


class Segment(Figure1D):
    def __init__(self, points: List[QPointF], color: QtGui.QColor = QtGui.QColor(QtCore.Qt.black)):
        super().__init__(points, color)

    def paint(self, scene: QtWidgets.QGraphicsScene):
        scene.addLine(QtCore.QLineF(self.first_pt, self.second_pt), self.color)
