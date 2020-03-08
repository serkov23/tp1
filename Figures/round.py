import math
from typing import List

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QPointF

from Figures.ellipse import Ellipse


class Round(Ellipse):
    def __init__(self, points: List[QPointF], color: QtGui.QColor = QtGui.QColor(QtCore.Qt.black),
                 inner_color: QtGui.QColor = QtGui.QColor(QtCore.Qt.white)):
        a = math.sqrt((points[0].x() - points[1].x()) ** 2 + (points[0].y() - points[1].y()) ** 2)

        super().__init__([QPointF(points[0].x() + a, points[0].y() + a), QPointF(points[0].x() - a, points[0].y() - a)],
                         color, inner_color)
