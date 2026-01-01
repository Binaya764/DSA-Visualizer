from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import QRectF, Qt

soft_blue   = QColor(100, 149, 237)


class StackVisualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.blocks = []

    def draw_stack(self, stack):
        self.scene.clear()
        self.blocks.clear()

        width = 80
        height = 40
        spacing = 5
        base_y = 250  # bottom of stack

        # Draw stack blocks
        for i, val in enumerate(stack):
            x = 100
            y = base_y - (i + 1) * (height + spacing)

            rect = QGraphicsRectItem(QRectF(x, y, width, height))
            rect.setBrush(QBrush(Qt.darkCyan))

            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + 30, y + 10)

            self.scene.addItem(rect)
            self.scene.addItem(text)
            self.blocks.append((rect, text))

        # Draw TOP label
        if stack:
            top_label = QGraphicsSimpleTextItem("TOP")
            top_label.setBrush(Qt.yellow)
            top_label.setPos(190, base_y - len(stack)*(height+spacing))
            self.scene.addItem(top_label)

    def highlight_top(self):
        if self.blocks:
            self.blocks[-1][0].setBrush(QBrush(Qt.red))



