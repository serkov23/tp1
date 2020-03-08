import typing

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsSceneMouseEvent

from Model import Model


class MGraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self, scene_rect: QtCore.QRectF,
                 parent: typing.Optional[QtWidgets.QWidget] = None):
        self.model = None
        super(MGraphicsScene, self).__init__(scene_rect, parent)

    def set_model(self, model: Model):
        self.model = model

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.model.add_point(event.scenePos())
        super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.model.double_clicked()
        super().mouseDoubleClickEvent(event)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key_Escape:
            self.model.double_clicked()
        super().keyPressEvent(event)
