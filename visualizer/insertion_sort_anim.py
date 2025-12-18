from PySide6.QtCore import QTimer

class InsertionSortAnimator:
    def __init__(self, canvas):
        self.canvas = canvas
        self.timer = QTimer()
        self.timer.timeout.connect(self.step)
        self.array = []
        self.i = 1
        self.j = None
        self.key = None
        self.phase = "compare"  # "compare", "shift", "insert"
        self.speed = 500

    def start(self, array):
        self.array = array[:]
        self.i = 1
        if len(self.array) > 1:
            self.key = self.array[self.i]
            self.j = self.i - 1
            self.phase = "compare"
            self.timer.start(self.speed)
        else:
            self.key = None

    def step(self):
        if self.i >= len(self.array):
            self.timer.stop()
            return

        if self.phase == "compare":
            # Highlight comparison
            if self.j >= 0 and self.array[self.j] > self.key:
                self.canvas.set_state({
                    "array": self.array.copy(),
                    "highlight": {"red": [self.j, self.j+1]},
                    "key": self.i
                })
                self.phase = "shift"
            else:
                self.phase = "insert"

        elif self.phase == "shift":
            # Shift element to the right
            self.array[self.j + 1] = self.array[self.j]
            self.canvas.set_state({
                "array": self.array.copy(),
                "highlight": {"red": [self.j, self.j+1]},
                "key": self.i
            })
            self.j -= 1
            # After shifting, go back to compare next element
            self.phase = "compare"

        elif self.phase == "insert":
            # Insert key into correct position
            self.array[self.j + 1] = self.key
            self.canvas.set_state({
                "array": self.array.copy(),
                "highlight": {"yellow": [self.j+1]},
                "key": self.i
            })
            # Move to next element
            self.i += 1
            if self.i < len(self.array):
                self.key = self.array[self.i]
                self.j = self.i - 1
                self.phase = "compare"
            else:
                self.timer.stop()
