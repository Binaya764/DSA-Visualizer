from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import QRectF, Qt

soft_blue   = QColor(100, 149, 237)
soft_green  = QColor(46, 125, 50)
soft_red    = QColor(240, 128, 128)
soft_gray   = QColor(200, 200, 200)
soft_yellow = QColor(240, 200, 120)

class SelectionSortVisualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.bars = []
        self.values = []
        self.y_offset = 10

    def draw_array(self, arr):

        self.bars.clear()
        self.values = arr.copy()
        width = 60
        spacing = 1
        y= self.y_offset
        self.y_offset += 100

        for i, val in enumerate(arr):
            height = 60
            x = i * (width + spacing)
            bar = QGraphicsRectItem(QRectF(x, y, width, height))
            bar.setBrush(QBrush(soft_red))

            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 20, y +15)

            self.scene.addItem(bar)
            self.scene.addItem(text)
            self.bars.append((bar, text))

            for i in range(len(arr)):
                    x = i * ( 60+ spacing)


                    index = QGraphicsSimpleTextItem(str(i))
                    index.setBrush(Qt.gray)
                    index.setPos(x+20, y+60)
                    self.scene.addItem(index)
        self.view.setSceneRect(self.scene.itemsBoundingRect())
        self.view.centerOn(self.bars[0][0])

    def draw_box_color(self):
            print("draw box called")
            #Box label for compare
            compare_box = QGraphicsRectItem(QRectF(350, -150, 20, 20))
            compare_box.setBrush(QBrush(soft_yellow))
            index_label= QGraphicsSimpleTextItem("Compare")
            index_label.setBrush(Qt.white)
            index_label.setPos(380,-150)
            self.scene.addItem(index_label)
            self.scene.addItem(compare_box)

            #Box label for swap
            swap_box = QGraphicsRectItem(QRectF(350, -120, 20, 20))
            swap_box.setBrush(QBrush(soft_blue))
            swap_label= QGraphicsSimpleTextItem("Swap")
            swap_label.setBrush(Qt.white)
            swap_label.setPos(380,-120)
            self.scene.addItem(swap_label)
            self.scene.addItem(swap_box)

            #Box label for unsorted
            unsorted_box = QGraphicsRectItem(QRectF(350, -90, 20, 20))
            unsorted_box.setBrush(QBrush(soft_red))
            unsorted_label= QGraphicsSimpleTextItem("Unsorted")
            unsorted_label.setBrush(Qt.white)
            unsorted_label.setPos(380,-90)
            self.scene.addItem(unsorted_label)
            self.scene.addItem(unsorted_box)
            self.y_offset = 10




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
