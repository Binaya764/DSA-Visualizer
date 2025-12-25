from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide6.QtGui import QBrush
from PySide6.QtCore import QRectF, Qt


class QueueVisualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.blocks = []   # stores (rect, text)

    def draw_queue(self, queue):
        self.scene.clear()
        self.blocks.clear()

        width = 80
        height = 40
        spacing = 10
        start_x = 100
        y = 180   # fixed horizontal line for queue

        # Draw queue blocks (left → right)
        for i, val in enumerate(queue):
            x = start_x + i * (width + spacing)

            rect = QGraphicsRectItem(QRectF(x, y, width, height))
            rect.setBrush(QBrush(Qt.darkGreen))

            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 30, y + 10)

            self.scene.addItem(rect)
            self.scene.addItem(text)
            self.blocks.append((rect, text))

        # Draw FRONT and REAR labels
        if queue:
            front_label = QGraphicsSimpleTextItem("FRONT")
            front_label.setBrush(Qt.yellow)
            front_label.setPos(start_x, y + height + 10)
            self.scene.addItem(front_label)

            rear_x = start_x + (len(queue) - 1) * (width + spacing)
            rear_label = QGraphicsSimpleTextItem("REAR")
            rear_label.setBrush(Qt.yellow)
            rear_label.setPos(rear_x, y + height + 10)
            self.scene.addItem(rear_label)

    def highlight_front(self):
        if self.blocks:
            self.blocks[0][0].setBrush(QBrush(Qt.red))
