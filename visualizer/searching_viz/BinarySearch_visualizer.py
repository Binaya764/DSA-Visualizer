from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import QRectF, Qt

class Binary_Visualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

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
        y = 200

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

        for i in range(len(arr)):
                    x = i * ( 60+ spacing)
                    y = 140

                    index = QGraphicsSimpleTextItem(str(i))
                    index.setBrush(Qt.gray)
                    index.setPos(x+20, y+60)
                    self.scene.addItem(index)

    def highlight(self, left, mid, right, color_mid=Qt.yellow, color_others=Qt.yellow):
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
            self.bars[index].setBrush(QBrush(Qt.green))



