from abc import ABC

from PyQt5.QtCore import QPointF

from Figures.Figure import Figure


class Figure1D(Figure, ABC):
    @staticmethod
    def points_needed() -> int:
        return 2

    @property
    def first_pt(self) -> QPointF:
        return self.points[0]

    @first_pt.setter
    def first_pt(self, val: QPointF):
        self.points[0] = val

    @property
    def second_pt(self) -> QPointF:
        return self.points[1]

    @second_pt.setter
    def second_pt(self, val: QPointF):
        self.points[1] = val
