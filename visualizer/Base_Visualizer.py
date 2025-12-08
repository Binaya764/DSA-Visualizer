# visualizers/base_visualizer.py
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsSimpleTextItem, QGraphicsRectItem
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import QRectF, Qt

class BaseVisualizer:
    def __init__(self, view):
        self.view = view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.bars = []
        self.values = []

    def clearScene(self):
        self.scene.clear()
        self.bars.clear()

    # ---------- COMMON FUNCTION USED BY BOTH SORT & SEARCH ----------
    def draw_array(self, arr):          #Draws array
        self.scene.clear()
        self.bars.clear()
        self.values = arr.copy()
        width = 60  # bar width
        spacing = 1  #spaing betwee the bars




        for i, val in enumerate(arr):
            height = 60
            x = i * (width + spacing)
            y = 200 - height

            bar = QGraphicsRectItem(QRectF(x, y, width, height))
            bar.setBrush(QBrush(Qt.lightGray))

            # Adding  number label
            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 20, y - 20)

            self.scene.addItem(bar)
            self.scene.addItem(text)
            self.bars.append((bar, text))

    def ref_drawArray(self, arr):
        self.clearScene()

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

            txt = QGraphicsSimpleTextItem(str(val))
            txt.setBrush(Qt.white)
            txt.setPos(x + 20, y + 15)

            self.scene.addItem(bar)
            self.scene.addItem(txt)

            self.bars.append((bar, txt))
