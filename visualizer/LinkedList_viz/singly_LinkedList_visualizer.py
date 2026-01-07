from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsSimpleTextItem
)
from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtCore import QRectF, Qt

# ================= COLORS =================
NODE_COLOR = QColor(100, 149, 237)   # Cornflower blue
TEXT_COLOR = Qt.white
ARROW_COLOR = Qt.white
LABEL_COLOR = Qt.lightGray

ADDRESS_START = 0x1000
ADDRESS_STEP = 0x10



class NodeVisualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.node_width = 60
        self.node_height = 50
        self.spacing = 30
        self.top_margin = 40

    # ======================================
    def draw_list(self, data_list, highlight_index=None):

        """
        Draws a singly linked list with:
        - HEAD label
        - TAIL label
        - Arrows
        - NULL pointer
        """
        self.scene.clear()

        if not data_list:
            return

        nodes = []

        # ---------- DRAW NODES ----------
        for i, val in enumerate(data_list):
            x = i * (self.node_width + self.spacing)
            y = self.top_margin

            # NODE RECT
            rect = QGraphicsRectItem(
                QRectF(x, y, self.node_width, self.node_height)
            )
            if highlight_index is not None:
                if i == highlight_index:
                    rect.setBrush(QBrush(QColor(220, 53, 69)))  # RED
                elif i == highlight_index - 1:
                    rect.setBrush(QBrush(QColor(255, 193, 7)))  # YELLOW (prev)
                else:
                    rect.setBrush(QBrush(NODE_COLOR))
            else:
                rect.setBrush(QBrush(NODE_COLOR))


            rect.setPen(QPen(Qt.black))
            self.scene.addItem(rect)

            # VALUE TEXT
            value_text = QGraphicsSimpleTextItem(str(val))
            value_text.setBrush(QBrush(TEXT_COLOR))
            value_text.setPos(
                x + self.node_width / 3,
                y + self.node_height / 4
            )
            self.scene.addItem(value_text)

            # -------- MEMORY ADDRESS --------
            address = ADDRESS_START + i * ADDRESS_STEP
            addr_text = QGraphicsSimpleTextItem(hex(address))
            addr_text.setBrush(QBrush(QColor(180, 180, 180)))
            addr_text.setPos(
                x + self.node_width / 6,
                y + self.node_height + 5
            )
            self.scene.addItem(addr_text)

            nodes.append(rect)

            # ARROW TO NEXT
            if i < len(data_list) - 1:
                self.scene.addLine(
                    x + self.node_width,
                    y + self.node_height / 2,
                    x + self.node_width + self.spacing,
                    y + self.node_height / 2,
                    QPen(ARROW_COLOR, 2)
                )


            # ---------- ARROW TO NEXT ----------
            if i < len(data_list) - 1:
                self.scene.addLine(
                    x + self.node_width,
                    y + self.node_height / 2,
                    x + self.node_width + self.spacing,
                    y + self.node_height / 2,
                    QPen(ARROW_COLOR, 2)
                )

        # ---------- HEAD LABEL ----------
        head = nodes[0]
        head_label = QGraphicsSimpleTextItem("HEAD")
        head_label.setBrush(QBrush(LABEL_COLOR))
        head_label.setPos(
            head.rect().x() + 5,
            head.rect().y() - 25
        )
        self.scene.addItem(head_label)

        # ---------- TAIL LABEL ----------
        tail = nodes[-1]
        tail_label = QGraphicsSimpleTextItem("TAIL")
        tail_label.setBrush(QBrush(LABEL_COLOR))
        tail_label.setPos(
            tail.rect().x() + 40,
            tail.rect().y() - 25
        )
        self.scene.addItem(tail_label)

        # ---------- ARROW TO NULL ----------
        null_x = tail.rect().x() + self.node_width + self.spacing
        null_y = tail.rect().y() + self.node_height / 2

        self.scene.addLine(
            tail.rect().x() + self.node_width,
            null_y,
            null_x - 5,
            null_y,
            QPen(ARROW_COLOR, 2)
        )

        # ---------- NULL LABEL ----------
        null_text = QGraphicsSimpleTextItem("NULL")
        null_text.setBrush(QBrush(LABEL_COLOR))
        null_text.setPos(null_x, null_y - 10)
        self.scene.addItem(null_text)

        # ---------- FINAL VIEW ADJUST ----------
        self.view.setSceneRect(self.scene.itemsBoundingRect())
        self.view.centerOn(nodes[0])
