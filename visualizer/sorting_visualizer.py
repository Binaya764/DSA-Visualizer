from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import QRectF, Qt


class sort_Visualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.bars = []       # stores QGraphicsRectItem
        self.values = []     # stores actual numbers

    # ----------------------------------------------------------------------
    # Draw the complete array (at start)
    # ----------------------------------------------------------------------
    def draw_array(self, arr):
        self.scene.clear()
        self.bars.clear()
        self.values = arr.copy()

        n = len(arr)

        width = 40  # bar width
        spacing = 10
        max_height = 250  # maximum height of bar

        max_val = max(arr)

        for i, val in enumerate(arr):
            height = (val / max_val) * max_height
            x = i * (width + spacing)
            y = 200 - height

            bar = QGraphicsRectItem(QRectF(x, y, width, height))
            bar.setBrush(QBrush(Qt.blue))

            # Add number label
            text = QGraphicsSimpleTextItem(str(val))
            text.setPos(x + 3, y - 20)

            self.scene.addItem(bar)
            self.scene.addItem(text)

            self.bars.append((bar, text))

    # ----------------------------------------------------------------------
    # Highlight bars (compare)
    # ----------------------------------------------------------------------
    def highlight(self, i, j, color):
        if 0 <= i < len(self.bars):
            self.bars[i][0].setBrush(QBrush(color))
        if 0 <= j < len(self.bars):
            self.bars[j][0].setBrush(QBrush(color))

    # ----------------------------------------------------------------------
    # Update bar positions after a swap
    # ----------------------------------------------------------------------
    def swap_bars(self, updated_array, i, j):
        """Redraws bars using new array state."""
        self.draw_array(updated_array)

