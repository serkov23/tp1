import math
from typing import List

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QPointF, QRectF

from Figures.segment import Segment


class Ray(Segment):

    def __init__(self, points: List[QPointF], color: QtGui.QColor = QtGui.QColor(QtCore.Qt.black)):
        super().__init__(points, color)

    INFINITY = 1e5

    @property
    def second_pt(self) -> QPointF:
        return self.recount_second_pt(self.first_pt, super().second_pt)

    @staticmethod
    def recount_second_pt(first_pt: QPointF, second_pt: QPointF) -> QPointF:
        x = second_pt.x() - first_pt.x()
        y = second_pt.y() - first_pt.y()

        phi = math.atan(x / y)+(math.pi if y<0 else 0)
        r = Ray.INFINITY
        return QPointF(first_pt.x() + r * math.sin(phi), first_pt.y() + r * math.cos(phi))
