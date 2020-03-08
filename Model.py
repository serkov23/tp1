from typing import Dict, Type, List

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QAction, QActionGroup, QGraphicsScene

from Figures.Figure import Figure
from Figures.point_figure import Point
from Figures.Figure2D import Figure2D


class Model:
    __cur_figure: Type[Figure]
    scene: QGraphicsScene
    pen_color: QColor
    brush_color: QColor
    __point_list: List[QtCore.QPointF]
    __actions: QActionGroup
    FIGURE_MAP: Dict[QAction, Type[Figure]]
    __figure_list: List[Figure]

    def __init__(self, figure_map: Dict[QtWidgets.QAction, Type[Figure]], actions: QtWidgets.QActionGroup,
                 scene: QtWidgets.QGraphicsScene, list_model: QtGui.QStandardItemModel):
        self.__point_list = []
        self.brush_color = QtGui.QColor(QtCore.Qt.transparent)
        self.pen_color = QtGui.QColor(QtCore.Qt.black)
        self.__figure_list = []
        self.__figure_map = figure_map
        self.__actions = actions
        self.scene = scene
        self.__cur_figure = self.__figure_map[self.__actions.checkedAction()]
        self.list_model = list_model

    def add_point(self, point: QtCore.QPointF):

        cur_figure = self.__figure_map[self.__actions.checkedAction()]
        self.__cmp_and_react(cur_figure)
        if len(self.__point_list)==0:
            if cur_figure.points_needed() == Figure.UNDEFINED_POINTS:
                cur_figure.point_amm = QtWidgets.QInputDialog.getInt(self.scene.parent(), "points amount", "int:",
                                                                     min=3, step=1)[0]
        if cur_figure.points_needed() == Figure.UNLIMITED_POINTS or cur_figure.points_needed() >= len(
                self.__point_list) - 1:
            self.__point_list.append(point)

        self.paint_figure(self.add_figure(Point, [point]))
        if cur_figure.points_needed() == len(self.__point_list):
            self.__finalize_figure()

    def double_clicked(self):
        cur_figure = self.__figure_map[self.__actions.checkedAction()]
        if cur_figure.points_needed() == Figure.UNLIMITED_POINTS:
            self.__finalize_figure()

    def __finalize_figure(self):
        self.add_figure(self.__cur_figure, self.__point_list)
        self.__clear_point_list()
        self.update()

    def __cmp_and_react(self, cur_figure):
        if cur_figure != self.__cur_figure:
            self.__clear_point_list()
            self.__cur_figure = cur_figure

    def __clear_point_list(self):
        if len(self.__figure_list) == 0:
            return
        self.__figure_list = self.__figure_list[:-len(self.__point_list) - 1] + [self.__figure_list[-1]]
        self.__point_list = []

    def add_figure(self, figure: Type[Figure], points: List[QtCore.QPointF]):
        self.__figure_list.append(figure(points, self.pen_color))
        if issubclass(figure, Figure2D):
            self.__figure_list[-1].set_inner_color(self.brush_color)
        return self.__figure_list[-1]

    def paint_figure(self, figure: Figure):
        figure.paint(self.scene)
        self.list_model.appendRow(QtGui.QStandardItem(str(figure)))
        self.scene.views()[0].update()

    def remove_figure(self, ind) -> bool:
        if len(self.__point_list) != 0:
            return False
        for i in ind:
            self.__figure_list.pop(i)
        self.update()
        return True

    def get_figure(self, ind: int) -> Figure:
        return self.__figure_list[ind]

    def update(self):
        self.list_model.clear()
        self.scene.clear()
        for i in self.__figure_list:
            i.paint(self.scene)
            self.list_model.appendRow(QtGui.QStandardItem(str(i)))
        self.scene.views()[0].update()
