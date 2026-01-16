from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import QRectF, Qt

soft_blue   = QColor(100, 149, 237)   # Cornflower blue
soft_green  =QColor(46, 125, 50) # Light green
soft_red    = QColor(240, 128, 128)   # Light coral
soft_gray   = QColor(200, 200, 200)   # Light gray
soft_purple = QColor(186, 160, 255)
soft_yellow = QColor(240, 200, 120)


class sort_Visualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.bars = []       # stores QGraphicsRectItem
        self.values = []     # stores actual numbers




    def draw_array(self, arr):          #Draws array
        print("draw_array called")
        #self.scene.clear()
        self.bars.clear()
        self.values = arr.copy()
        width = 60  # bar width
        spacing = 1  #spacing between the bars
        y =10


        for i, val in enumerate(arr):
            height = 60
            x = i * (60 + spacing)
            bar = QGraphicsRectItem(QRectF(x, y, width, height))
            bar.setBrush(QBrush(soft_red))

            # Adding  number label
            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 20, y + 15)

            self.scene.addItem(bar)
            self.scene.addItem(text)
            self.bars.append((bar, text))

        for i in range(len(arr)):
                x = i * ( 60+ spacing)

                index = QGraphicsSimpleTextItem(str(i))
                index.setBrush(Qt.gray)
                index.setPos(x+20, y+60)
                self.scene.addItem(index)

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

            #Box label for sorted
            sorted_box = QGraphicsRectItem(QRectF(350, -90, 20, 20))
            sorted_box.setBrush(QBrush(soft_green))
            sorted_label= QGraphicsSimpleTextItem("Sorted")
            sorted_label.setBrush(Qt.white)
            sorted_label.setPos(380,-90)
            self.scene.addItem(sorted_label)
            self.scene.addItem(sorted_box)

            #Box label for unsorted
            unsorted_box = QGraphicsRectItem(QRectF(350, -60, 20, 20))
            unsorted_box.setBrush(QBrush(soft_red))
            unsorted_label= QGraphicsSimpleTextItem("Unsorted")
            unsorted_label.setBrush(Qt.white)
            unsorted_label.setPos(380,-60)
            self.scene.addItem(unsorted_label)
            self.scene.addItem(unsorted_box)






    #High lights the color of the bar
    def highlight(self, i, j, color):
        if 0 <= i < len(self.bars):
            self.bars[i][0].setBrush(QBrush(color))
        if 0 <= j < len(self.bars):
            self.bars[j][0].setBrush(QBrush(color))


   #Updates the bar position after swapping
    def swap_bars(self, updated_array, i, j):
        self.draw_array(updated_array)

    def completed_sort(self): #colors the bar green once the sorting is completed
        for bar in self.bars:
         rect, text = bar
         rect.setBrush(soft_green)
         self.y_offset = 10
         self.values.clear()


class ref_Visualizer:
    def __init__(self, graphics_view2):
            self.view = graphics_view2
            self.scene = QGraphicsScene()
            self.view.setScene(self.scene)

            self.bars = []       # stores QGraphicsRectItem
            self.values = []
            self.indexes =[]

    def ref_drawArray(self,arr):
            self.scene.clear()
            self.bars.clear()
            self.values = arr.copy()
            width = 50  # bar width
            spacing = 1  #spcaing between the bars

            label = QGraphicsSimpleTextItem("Original:") #adds original label to the array
            label.setBrush(Qt.white)
            label.setPos(-60, -210)
            self.scene.addItem(label)





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

            #Adding index label
            index_label= QGraphicsSimpleTextItem("Index:")
            index_label.setBrush(Qt.white)
            index_label.setPos(-52,-180)
            self.scene.addItem(index_label)


            for i in range(len(arr)):
                x = i * ( 50+ spacing)
                y = -230

                index = QGraphicsSimpleTextItem(str(i))
                index.setBrush(Qt.gray)
                index.setPos(x+20, y+53)
                self.scene.addItem(index)






class code_Visualizer:
        def __init__(self,graphics_View3):
                self.view = graphics_View3
                self.scene = QGraphicsScene()
                self.view.setScene(self.scene)
                self.codes=[]  #stores code

                text = QGraphicsSimpleTextItem("Hello world")
                text.setBrush(Qt.white)
                self.scene.addItem(text)


