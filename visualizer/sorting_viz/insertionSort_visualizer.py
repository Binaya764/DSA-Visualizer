from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsSimpleTextItem,
)
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import QRectF, Qt

soft_blue   = QColor(100, 149, 237)
soft_green  = QColor(144, 238, 144)
soft_red    = QColor(240, 128, 128)
soft_gray   = QColor(200, 200, 200)
soft_yellow = QColor(240, 200, 120)


class InsertionSortVisualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.bars = []

    def draw_array(self, arr):
        self.scene.clear()
        self.bars.clear()

        width = 50
        spacing = 10
        base_y = 150

        for i, val in enumerate(arr):
            height = val * 2
            x = i * (width + spacing)
            y = base_y - height

            bar = QGraphicsRectItem(QRectF(x, y, width, height))
            bar.setBrush(QBrush(soft_gray))

            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 10, base_y + 5)

            self.scene.addItem(bar)
            self.scene.addItem(text)
            self.bars.append(bar)

    def highlight(self, i, j, color):
        if 0 <= i < len(self.bars):
            self.bars[i].setBrush(QBrush(color))
        if 0 <= j < len(self.bars):
            self.bars[j].setBrush(QBrush(color))

    def completed_sort(self):
        for bar in self.bars:
            bar.setBrush(QBrush(soft_green))
