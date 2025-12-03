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

    #High lights the color of the bar
    def highlight(self, i, j, color):
        if 0 <= i < len(self.bars):
            self.bars[i][0].setBrush(QBrush(color))
        if 0 <= j < len(self.bars):
            self.bars[j][0].setBrush(QBrush(color))

   #Updates the bar position after swapping
    def swap_bars(self, updated_array, i, j):
        """Redraws bars using new array state."""
        self.draw_array(updated_array)

    def completed_sort(self): #colors the bar green once the sorting is completed
        for bar in self.bars:
         rect, text = bar
         rect.setBrush(Qt.green)

class ref_Visualizer:
    def __init__(self, graphics_view2):
            self.view = graphics_view2
            self.scene = QGraphicsScene()
            self.view.setScene(self.scene)

            self.bars = []       # stores QGraphicsRectItem
            self.values = []

    def ref_drawArray(self,arr):
            self.scene.clear()
            self.bars.clear()
            self.values = arr.copy()
            width = 50  # bar width
            spacing = 1  #spcaing between the bars




            for i, val in enumerate(arr):
                height = 50
                x = i * (50 + spacing)
                y = -230

                bar = QGraphicsRectItem(QRectF(x, y, width, height))
                bar.setBrush(QBrush(Qt.darkGray))

                # Adding  number label
                text = QGraphicsSimpleTextItem(str(val))
                text.setBrush(Qt.white)
                text.setPos(x + 20, y + 15)

                self.scene.addItem(bar)
                self.scene.addItem(text)
                self.bars.append((bar, text))




class code_Visualizer:
        def __init__(self,graphics_View3):
                self.view = graphics_View3
                self.scene = QGraphicsScene()
                self.view.setScene(self.scene)
                self.codes=[]  #stores code

                text = QGraphicsSimpleTextItem("Hello world")
                text.setBrush(Qt.white)
                self.scene.addItem(text)


