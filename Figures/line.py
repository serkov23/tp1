from typing import List

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QPointF

from Figures.figure1D import Figure1D
from Figures.ray import Ray
from id_producer import IdProducer


class Line(Figure1D):
    cur_id = IdProducer()

    def __init__(self, points: List[QPointF], color: QtGui.QColor = QtGui.QColor(QtCore.Qt.black)):
        self.ray1 = Ray(points, color)
        self.ray2 = Ray([points[1], points[0]], color)
        super().__init__(points, color)

    def paint(self, scene: QtWidgets.QGraphicsScene):
        self.ray1.paint(scene)
        self.ray2.paint(scene)

    @property
    def first_pt(self) -> QPointF:
        return self.ray2.second_pt

    @property
    def second_pt(self) -> QPointF:
        return self.ray1.second_pt

    @property
    def color(self) -> QtGui.QColor:
        return self.ray1.color

    @color.setter
    def color(self, color: QtGui.QColor):
        self.ray1.color = color
        self.ray2.color = color
