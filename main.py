from PyQt6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
from algorithms.Bubble_sort import bubble_sort
from visualizer.array_visualizer import ArrayVisualizer
from PyQt6.QtCore import QTimer
from widget import Widget
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.visualizer = ArrayVisualizer()
        self.visualizer2 = CodeVisualizer()
        self.ui.visualAreaLayout.addWidget(self.visualizer)
        self.ui.visualAreaLayout.addWidget(self.visualizer2)

        # Connect button
        self.ui.runButton.clicked.connect(self.run_visualization)

        self.steps = []
        self.current_step = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    def run_visualization(self):
        arr = [5, 3, 8, 2, 1]   # get from input box later
        self.steps = bubble_sort(arr)
        self.current_step = 0
        self.timer.start(300)   # 300ms per frame

    def update_frame(self):
        if self.current_step >= len(self.steps):
            self.timer.stop()
            return

        step = self.steps[self.current_step]
        self.visualizer.draw(step["array"], step["highlight"])
        self.current_step += 1


app = QApplication([])
window = Main()
window.show()
app.exec()
