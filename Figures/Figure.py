from abc import ABC, abstractmethod
from typing import List

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QPointF

from id_producer import IdProducer


class Figure(ABC):
    def __init__(self, points: List[QPointF], color: QtGui.QColor = QtGui.QColor(QtCore.Qt.black)):
        if self.points_needed() > 0 and len(points) != self.points_needed():
            raise self.PointNumberException(self.points_needed(), len(points))
        self.color = color
        self.__points = points
        self.id = self.get_next_id()

    UNLIMITED_POINTS = -1
    UNDEFINED_POINTS = -2
    cur_id = IdProducer()

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        self.__points = value

    def __str__(self):
        return "{type} {id}".format(type=self.__class__.__name__, id=str(self.id))

    @classmethod
    def get_next_id(cls) -> int:
        return cls.cur_id.produce(cls)

    @staticmethod
    def points_needed() -> int:
        return 0

    @abstractmethod
    def paint(self, scene: QtWidgets.QGraphicsScene):
        pass

    def move(self, pt: QPointF):
        sx, sy = 0, 0
        for i in self.points:
            sx += i.x()
            sy += i.y()
        sx /= len(self.points)
        sy /= len(self.points)
        dx = sx - pt.x()
        dy = sy - pt.y()
        for i in self.points:
            i.setX(i.x() - dx)
            i.setY(i.y() - dy)

    def __del__(self):
        self.cur_id.ret_id(self.id, self.__class__)

    class PointNumberException(Exception):
        def __init__(self, expected: int, found: int, msg: str = ""):
            super().__init__(
                "invalid point number: expected {exp}, found {fnd};\n".format(exp=expected, fnd=found) + msg)
