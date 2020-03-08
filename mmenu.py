import typing

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from Model import Model


class MMenu(QtWidgets.QMenu):
    model: typing.Optional[Model]
    list_view: typing.Optional[QtWidgets.QListView]

    def __init__(self, parent: typing.Optional['QWidget'] = ...) -> None:
        super(MMenu, self).__init__(parent)
        self.__list_view = None
        self.model = None

    def set_list_view(self, lw: QtWidgets.QListView):
        self.__list_view = lw

    def set_model(self, lw: QtWidgets.QListView):
        self.__list_view = lw

    def aboutToShow(self) -> None:
        print("1")

        super().aboutToShow()
