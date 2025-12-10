from PySide6.QtWidgets import QWidget, QGraphicsScene, QApplication
from PySide6.QtCore import QTimer, Qt
from ui_insertion_sort import Ui_Widget
from sorter import insertion_sort_steps
from animation import InsertionSortAnimation

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create a scene for the graphics view
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        # Setup animation with the scene
        self.animation = InsertionSortAnimation(self.scene)

        # Sorting data
        self.array = []
        self.steps = []
        self.current_step = 0

        # Timer for animation
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_step)

        # Connect buttons
        self.ui.btnGenerate.clicked.connect(self.generate_array)
        self.ui.btnSort.clicked.connect(self.start_sort)

    def generate_array(self):
        """Parse input and draw initial bars"""
        text = self.ui.inputArray.text()
        try:
            self.array = list(map(int, text.split(',')))
        except ValueError:
            self.ui.statusLabel.setText("Invalid input!")
            return

        if not self.array:
            self.ui.statusLabel.setText("Enter at least one number")
            return

        self.ui.statusLabel.setText("Array generated")
        self.animation.draw_array(self.array)

    def start_sort(self):
        """Prepare steps and start timer animation"""
        if not self.array:
            self.ui.statusLabel.setText("Generate array first!")
            return

        # Get all sorting steps
        self.steps = insertion_sort_steps(self.array[:])
        self.current_step = 0
        self.timer.start(400)  # animation speed in milliseconds
        self.ui.statusLabel.setText("Sorting...")

    def next_step(self):
        """Perform next sorting step"""
        if self.current_step >= len(self.steps):
            self.timer.stop()
            self.ui.statusLabel.setText("Sorting complete!")
            self.animation.draw_array(self.array)  # final state
            return

        arr, positions, highlight = self.steps[self.current_step]
        self.array = arr
        self.animation.update_bars(arr, positions, highlight)
        self.current_step += 1

# Run the widget standalone
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec())
