from abc import ABC
from typing import List

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QPointF

from Figures.Figure import Figure


class Figure2D(Figure, ABC):
    def __init__(self, points: List[QPointF], color: QtGui.QColor = QtGui.QColor(QtCore.Qt.black),
                 inner_color: QtGui.QColor = QtGui.QColor(QtCore.Qt.white)):
        super().__init__(points, color)
        self.inner_color = inner_color

    def set_inner_color(self, color: QtGui.QColor):
        self.inner_color = color

    def get_inner_color(self) -> QtGui.QColor:
        return self.inner_color