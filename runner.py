from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui

from Figures import Figure2D, rect, polygon, segment, ray, line, elipse
from Figures.poly_line import PolyLine
from Figures.regular_polygon import RegularPolygon
from Figures.round import Round
from MGraphicsScene import MGraphicsScene
from model import MModel
from main import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.figures = QtWidgets.QActionGroup(self)
        self.figures.addAction(self.ui.actionRect)
        self.figures.addAction(self.ui.actionPolygon)
        self.figures.addAction(self.ui.actionright_polygon)
        self.figures.addAction(self.ui.actionelipse)
        self.figures.addAction(self.ui.actionround)
        self.figures.addAction(self.ui.actionsegment)
        self.figures.addAction(self.ui.actionray)
        self.figures.addAction(self.ui.actionline)
        self.figures.addAction(self.ui.actionpoly_line)

        self.figures.setExclusive(True)
        act_map = {
            self.ui.actionPolygon: polygon.Polygon,
            self.ui.actionRect: rect.Rect,
            self.ui.actionsegment: segment.Segment,
            self.ui.actionray: ray.Ray,
            self.ui.actionline: line.Line,
            self.ui.actionelipse: elipse.Elipse,
            self.ui.actionround: Round,
            self.ui.actionright_polygon: RegularPolygon,
            self.ui.actionpoly_line: PolyLine
        }
        self.scene = MGraphicsScene(QtCore.QRectF(self.ui.graphicsView.rect()), self)
        self.list_model = QtGui.QStandardItemModel(self)
        self.model = MModel(act_map, self.figures, self.scene, self.list_model)
        self.scene.set_model(self.model)
        self.ui.listView.setModel(self.list_model)
        self.ui.listView.customContextMenuRequested.connect(
            lambda point: (self.edit_menu_check(), self.ui.menuedit.exec(self.ui.listView.mapToGlobal(point))))
        self.ui.graphicsView.setScene(self.scene)

        self.ui.action_pen_color.triggered.connect(self.choose_pen_color)
        self.ui.actionbrush_color.triggered.connect(self.choose_brush_color)
        self.ui.actionchange_brush.triggered.connect(self.change_brush_color)
        self.ui.actionchange_pen.triggered.connect(self.change_pen_color)
        self.ui.menuedit.set_model(self.model)
        self.ui.menuedit.set_list_view(self.ui.listView)
        self.ui.menuedit.menuAction().hovered.connect(self.edit_menu_check)

    def edit_menu_check(self):
        self.ui.menuedit.actions()[0].setEnabled(True)
        self.ui.menuedit.actions()[1].setEnabled(True)
        self.ui.menuedit.actions()[2].setEnabled(True)
        if self.ui.listView is None:
            raise Exception("list view isn't initialised")
        elif len(self.ui.listView.selectedIndexes()) == 0:
            self.ui.menuedit.actions()[0].setEnabled(False)
            self.ui.menuedit.actions()[1].setEnabled(False)
            self.ui.menuedit.actions()[2].setEnabled(False)
            return
        if len(self.ui.listView.selectedIndexes()) != 1:
            self.ui.menuedit.actions()[2].setEnabled(False)

        for i in self.ui.listView.selectedIndexes():
            if not isinstance(self.model.get_figure(i.row()), Figure2D.Figure2D):
                self.ui.menuedit.actions()[1].setEnabled(False)
                break

    def change_pen_color(self):
        d = QtWidgets.QColorDialog.getColor(initial=self.model.pen_color, parent=self)
        if d.isValid():
            for i in self.ui.listView.selectedIndexes():
                self.model.get_figure(i.row()).color = d
            self.model.update()

    def change_brush_color(self):
        d = QtWidgets.QColorDialog.getColor(initial=self.model.pen_color, parent=self)
        if d.isValid():
            for i in self.ui.listView.selectedIndexes():
                f = self.model.get_figure(i.row())
                if isinstance(f, Figure2D.Figure2D):
                    f.inner_color = d
                else:
                    QtWidgets.QErrorMessage(self).showMessage("can't change inner color of not 2D figure")
            self.model.update()

    def choose_pen_color(self, attr):
        d = QtWidgets.QColorDialog.getColor(initial=self.model.pen_color, parent=self)
        if d.isValid():
            self.model.pen_color = d

    def choose_brush_color(self, attr):
        d = QtWidgets.QColorDialog.getColor(initial=self.model.brush_color, parent=self)
        if d.isValid():
            self.model.brush_color = d

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == QtCore.Qt.Key_Delete:
            if not self.model.remove_figure(map(lambda x: x.row(), self.ui.listView.selectedIndexes())):
                QtWidgets.QErrorMessage(self).showMessage("you cannot delete while editing figure")
        super().keyPressEvent(a0)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())
