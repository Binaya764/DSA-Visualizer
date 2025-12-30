from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import QRectF, Qt

soft_blue   = QColor(100, 149, 237)
soft_green  = QColor(46, 125, 50)
soft_red    = QColor(240, 128, 128)
soft_gray   = QColor(200, 200, 200)

class SelectionSortVisualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.bars = []
        self.values = []

    def draw_array(self, arr):
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

            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 20, y - 20)

            self.scene.addItem(bar)
            self.scene.addItem(text)
            self.bars.append((bar, text))

            for i in range(len(arr)):
                    x = i * ( 60+ spacing)
                    y = 10

                    index = QGraphicsSimpleTextItem(str(i))
                    index.setBrush(Qt.gray)
                    index.setPos(x+20, y+60)
                    self.scene.addItem(index)

    def highlight(self, i, j, color):
        if 0 <= i < len(self.bars):
            self.bars[i][0].setBrush(QBrush(color))
        if 0 <= j < len(self.bars):
            self.bars[j][0].setBrush(QBrush(color))

    def swap_bars(self, updated_array, i, j):
        self.draw_array(updated_array)

    def completed_sort(self):
        for bar in self.bars:
            rect, text = bar
            rect.setBrush(soft_green)
