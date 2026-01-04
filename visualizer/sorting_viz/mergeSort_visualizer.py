from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import QRectF, Qt, QTimer

# Colors
soft_blue   = QColor(100, 149, 237)
soft_green  = QColor(46, 125, 50)
soft_red    = QColor(240, 128, 128)
soft_gray   = QColor(200, 200, 200)
soft_yellow = QColor(240, 200, 120)

class mergeSortVisualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.bars = []          # main list of all bars
        self.timer_delay = 500
        self.max_width = 800    # max horizontal space for bars

    def clear(self):
        self.scene.clear()
        self.bars.clear()

    def draw_subarray(self, arr, x_start=0, y_start=0):
        n = len(arr)
        if n == 0:
            return []

        total_space = self.max_width
        spacing = 5
        width = min(50, (total_space - spacing*(n-1)) / n)

        sub_bars = []
        for i, val in enumerate(arr):
            x = x_start + i * (width + spacing)
            y = y_start
            rect = QGraphicsRectItem(QRectF(x, y, width, 50))
            rect.setBrush(QBrush(soft_red))
            text = QGraphicsSimpleTextItem(str(val))
            text.setBrush(Qt.white)
            text.setPos(x + width/4, y + 15)
            self.scene.addItem(rect)
            self.scene.addItem(text)
            sub_bars.append((rect, text))

        # Keep reference in self.bars to prevent deletion
        self.bars.extend(sub_bars)
        return sub_bars

    def highlight(self, bar_tuple, color):
        rect, _ = bar_tuple
        rect.setBrush(QBrush(color))

    def start_sort(self, arr):
        self.clear()
        self._merge_sort_step(arr, 0, 0, lambda _: None)

    def _merge_sort_step(self, arr, x_start, y_start, callback):
        if len(arr) <= 1:
            bars = self.draw_subarray(arr, x_start, y_start)
            QTimer.singleShot(self.timer_delay, lambda: callback(arr))
            return

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        def left_done(left_sorted):
            def right_done(right_sorted):
                total_len = len(left_sorted) + len(right_sorted)
                merged = [0] * total_len
                merged_bars = self.draw_subarray(merged, x_start, y_start)

                i = j = k = 0

                def merge_step():
                    nonlocal i, j, k
                    if k >= total_len:
                        for rect, text in merged_bars:
                            self.highlight((rect, text), soft_green)
                        callback(merged)
                        return

                    if i < len(left_sorted) and (j >= len(right_sorted) or left_sorted[i] <= right_sorted[j]):
                        val = left_sorted[i]
                        i += 1
                    else:
                        val = right_sorted[j]
                        j += 1

                    merged[k] = val
                    rect, text = merged_bars[k]
                    text.setText(str(val))
                    self.highlight((rect, text), soft_blue)
                    k += 1
                    QTimer.singleShot(self.timer_delay, merge_step)

                merge_step()

            # Adjust x_start for right subarray
            right_x = x_start + mid * (min(50, (self.max_width - 5*(len(right)-1))/len(right)) + 5)
            self._merge_sort_step(right, right_x, y_start + 80, right_done)

        self._merge_sort_step(left, x_start, y_start + 80, left_done)
