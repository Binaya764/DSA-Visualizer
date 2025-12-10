# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
# animation.py
from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem
from PySide6.QtGui import QBrush
from PySide6.QtCore import Qt

class InsertionSortAnimation:
    def __init__(self, scene):
        self.scene = scene
        self.rects = []
        self.texts = []

    def draw_array(self, array):
        self.scene.clear()
        self.rects = []
        self.texts = []

        if not array:
            return

        max_val = max(array)
        width = 40
        spacing = 10

        for i, value in enumerate(array):
            height = (value / max_val) * 200
            rect = QGraphicsRectItem(0, 0, width, height)
            rect.setBrush(QBrush(Qt.blue))
            rect.setPos(i * (width + spacing), 250 - height)
            self.scene.addItem(rect)
            self.rects.append(rect)

            text = QGraphicsTextItem(str(value))
            text.setDefaultTextColor(Qt.black)
            text.setPos(i * (width + spacing) + width/4, 250 - height - 20)
            self.scene.addItem(text)
            self.texts.append(text)

    def update_bars(self, array, positions, highlight):
        width = 40
        spacing = 10
        for i, rect_index in enumerate(positions):
            self.rects[rect_index].setPos(i * (width + spacing), 250 - self.rects[rect_index].rect().height())
            self.texts[rect_index].setPos(i * (width + spacing) + width/4, 250 - self.rects[rect_index].rect().height() - 20)

        for i, rect in enumerate(self.rects):
            if i in highlight:
                rect.setBrush(QBrush(Qt.red))
            else:
                rect.setBrush(QBrush(Qt.blue))
