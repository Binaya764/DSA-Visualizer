from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import QRectF, Qt

soft_blue   = QColor(100, 149, 237)   # Cornflower blue
soft_green  = QColor(27, 94, 32)   # Light green
soft_red    = QColor(240, 128, 128)   # Light coral
soft_gray   = QColor(200, 200, 200)   # Light gray
soft_purple = QColor(186, 160, 255)
soft_yellow = QColor(240, 200, 120)


class Binary_Visualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.y_offset = 200

        self.row = 0
        self.bars = []       # store bar items
        self.values = []     # store actual numbers

    def draw_array(self, arr):
        """Draws the full array as bars."""
        print("Binary search array")
        self.scene.clear()
        self.bars.clear()
        self.values = arr.copy()
        width = 60
        spacing = 1
        y = self.y_offset

        for i, val in enumerate(arr):
            height = 60
            x = i * (width + spacing)
            bar = QGraphicsRectItem(QRectF(x, y - height, width, height))
            bar.setBrush(QBrush(Qt.lightGray))

            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 20, y - height + 20)

            self.scene.addItem(bar)
            self.scene.addItem(text)
            self.bars.append(bar)
        self.y_offset +=70

        for i in range(len(arr)):
                    x = i * ( 60+ spacing)
                    y = 140

                    index = QGraphicsSimpleTextItem(str(i))
                    index.setBrush(Qt.gray)
                    index.setPos(x+20, y+60)
                    self.scene.addItem(index)

    def highlight(self, left, mid, right, color_mid=soft_yellow, color_others=soft_yellow):
        """Highlight left, mid, right elements during search."""
        for i, bar in enumerate(self.bars):
            if i == mid:
                bar.setBrush(QBrush(color_mid))
            elif i == left or i == right:
                bar.setBrush(QBrush(color_others))
            else:
                bar.setBrush(QBrush(Qt.lightGray))

    def clear(self):
        """Clear the scene."""
        self.scene.clear()
        self.bars.clear()
        self.values.clear()

    def found(self, index):
        """Highlight the found element in green."""
        if 0 <= index < len(self.bars):
            self.bars[index].setBrush(QBrush(soft_green))



