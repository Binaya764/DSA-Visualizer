# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import QRectF, Qt

# Colors
soft_blue   = QColor(100, 149, 237)
soft_green  = QColor(144, 238, 144)
soft_red    = QColor(240, 128, 128)
soft_gray   = QColor(200, 200, 200)
soft_purple = QColor(186, 160, 255)


class mergeSort_Visualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.bars = []       # stores QGraphicsRectItem
        self.values = []     # stores actual numbers

    def draw_array(self, arr):          # Draws array
        self.scene.clear()
        self.bars.clear()
        self.values = arr.copy()
        width = 60
        spacing = 1

        for i, val in enumerate(arr):
            height = 60
            x = i * (width + spacing)
            y = 10

            bar = QGraphicsRectItem(QRectF(x, y, width, height))
            bar.setBrush(QBrush(soft_red))

            # Adding number label
            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 20, y - 20)

            self.scene.addItem(bar)
            self.scene.addItem(text)
            self.bars.append((bar, text))

    def highlight(self, i, j, color):
        if 0 <= i < len(self.bars):
            self.bars[i][0].setBrush(QBrush(color))
        if 0 <= j < len(self.bars):
            self.bars[j][0].setBrush(QBrush(color))

    def swap_bars(self, updated_array, i, j):
        """Redraws bars using new array state."""
        self.draw_array(updated_array)

    def completed_sort(self):  # colors the bar green once sorting is done
        for bar in self.bars:
            rect, text = bar
            rect.setBrush(soft_green)


class ref_Visualizer:
    def __init__(self, graphics_view2):
        self.view = graphics_view2
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.bars = []
        self.values = []

    def ref_drawArray(self, arr):
        self.scene.clear()
        self.bars.clear()
        self.values = arr.copy()
        width = 50
        spacing = 1

        label = QGraphicsSimpleTextItem("Original:")
        label.setBrush(Qt.white)
        label.setPos(-60, -210)
        self.scene.addItem(label)

        for i, val in enumerate(arr):
            height = 50
            x = i * (width + spacing)
            y = -230

            bar = QGraphicsRectItem(QRectF(x, y, width, height))
            bar.setBrush(QBrush(Qt.darkGray))

            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 20, y + 15)

            self.scene.addItem(bar)
            self.scene.addItem(text)
            self.bars.append((bar, text))

        # Index labels
        index_label = QGraphicsSimpleTextItem("Index:")
        index_label.setBrush(Qt.white)
        index_label.setPos(-52, -180)
        self.scene.addItem(index_label)

        for i in range(len(arr)):
            x = i * (width + spacing)
            y = -230
            index = QGraphicsSimpleTextItem(str(i))
            index.setBrush(Qt.gray)
            index.setPos(x + 20, y + 53)
            self.scene.addItem(index)


class code_Visualizer:
    def __init__(self, graphics_view3):
        self.view = graphics_view3
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.codes = []

        # Example placeholder text
        text = QGraphicsSimpleTextItem("Merge Sort Code Will Appear Here")
        text.setBrush(Qt.white)
        self.scene.addItem(text)
