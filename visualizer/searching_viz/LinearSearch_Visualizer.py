from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide6.QtGui import QBrush
from PySide6.QtCore import QRectF, Qt


class Linear_Visualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.bars = []      # store bar items
        self.values = []    # store actual values

    def draw_array(self, arr):
        """Draw the full array as bars (same look as Binary_Visualizer)."""
        self.scene.clear()
        self.bars.clear()
        self.values = arr.copy()

        width = 60
        spacing = 1
        y = 200

        for i, val in enumerate(arr):
            height = 60
            x = i * (width + spacing)

            bar = QGraphicsRectItem(QRectF(x, y - height, width, height))
            bar.setBrush(QBrush(Qt.lightGray))

            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 20, y - height - 20)

            self.scene.addItem(bar)
            self.scene.addItem(text)
            self.bars.append(bar)

    def highlight(self, index):
        """
        Highlight the currently compared element.
        All previous and next elements remain default.
        """
        for i, bar in enumerate(self.bars):
            if i == index:
                bar.setBrush(QBrush(Qt.yellow))
            else:
                bar.setBrush(QBrush(Qt.lightGray))

    def found(self, index):
        """Highlight the found element in green."""
        if 0 <= index < len(self.bars):
            self.bars[index].setBrush(QBrush(Qt.green))

    def clear(self):
        """Clear the scene."""
        self.scene.clear()
        self.bars.clear()
        self.values.clear()
