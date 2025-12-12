from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem
from PySide6.QtCore import QTimer, Qt

class AnimationBase:
    def __init__(self, scene: QGraphicsScene, array: list[int], rect_width: int = 20, rect_spacing: int = 5):
        self.scene = scene
        self.array = array[:]
        self.rect_width = rect_width
        self.rect_spacing = rect_spacing
        self.rects = []
        self.timer = QTimer()
        self.step_index = 0
        self._create_rects()

    def _create_rects(self):
        """Draw initial rectangles for the array"""
        self.scene.clear()
        self.rects = []
        for i, value in enumerate(self.array):
            rect = QGraphicsRectItem(i * (self.rect_width + self.rect_spacing), 0, self.rect_width, value*5)
            rect.setBrush(Qt.blue)
            self.scene.addItem(rect)
            self.rects.append(rect)

    def animate_step(self):
        """Override this in child classes"""
        pass

    def start_animation(self, interval: int = 500):
        """Start animation"""
        self.timer.timeout.connect(self.animate_step)
        self.timer.start(interval)

    def stop_animation(self):
        self.timer.stop()
