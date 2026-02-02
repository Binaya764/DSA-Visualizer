from PySide6.QtWidgets import (
    QGraphicsScene, QGraphicsRectItem, QGraphicsSimpleTextItem,
    QGraphicsLineItem, QGraphicsPolygonItem, QGraphicsEllipseItem
)
from PySide6.QtGui import QBrush, QPen, QColor, QPainter, QPolygonF, QFont
from PySide6.QtCore import Qt, QTimer, QPointF, QRectF
import math
import random

soft_blue = QColor(100, 149, 237)
soft_green = QColor(76, 175, 80)
soft_red = QColor(244, 67, 54)
soft_yellow = QColor(240, 200, 120)
soft_gray = QColor(200, 200, 200)
soft_purple = QColor(156, 39, 176)
soft_orange = QColor(255, 152, 0)

#Node
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.address = random.randint(1000,9999)

def draw_arrow(scene, x1, y1, x2, y2, color=Qt.white, width=2):
    #Draw an arrow from (x1, y1) to (x2, y2)
    # Draw the main line
    line = QGraphicsLineItem(x1, y1, x2, y2)
    line.setPen(QPen(color, width))
    scene.addItem(line)

    # Calculate angle of the line
    angle = math.atan2(y2 - y1, x2 - x1)

    # Arrowhead size
    arrow_size = 10

    # Calculate two points for the arrowhead triangle
    p1 = QPointF(
        x2 - (arrow_size * math.cos(angle - math.pi / 6)),
        y2 - arrow_size * math.sin(angle - math.pi / 6)
    )
    p2 = QPointF(
        x2 - arrow_size * math.cos(angle + math.pi / 6),
        y2 - arrow_size * math.sin(angle + math.pi / 6)
    )

    # Create the triangle polygon
    arrow_head = QPolygonF([QPointF(x2, y2), p1, p2])
    arrow_item = QGraphicsPolygonItem(arrow_head)
    arrow_item.setBrush(QBrush(color))
    arrow_item.setPen(QPen(color))
    scene.addItem(arrow_item)


class LinkedListVisualizer:
    def __init__(self, graphics_view):
        self.view = graphics_view
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        # Node dimensions
        self.node_width = 90
        self.node_height = 50
        self.gap = 40
        self.start_x = 30
        self.start_y = 80
        self.end_x = 90
        self.end_y = 80
        self.offset_end = 0


        # Data structures
        self.nodes = []  # list of ListNode
        self.graphics_nodes = {}
        self.head = None
        self.tail = None

        # Animation
        self.steps = []
        self.step_index = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_step)
        self.animation_speed = 500

        # Render settings
        self.view.setRenderHint(QPainter.Antialiasing, True)
        self.view.setRenderHint(QPainter.TextAntialiasing, True)



    def draw_list_head(self):
        self.scene.clear()
        self.graphics_nodes.clear()


        # Draw head label

        print("HEAD")
        head_label = QGraphicsSimpleTextItem("HEAD")
        head_label.setBrush(soft_yellow)
        font = QFont("Arial", 10, QFont.Bold)
        head_label.setFont(font)
        head_label.setPos(self.start_x-20+self.node_width/2, self.start_y - 40)
        self.scene.addItem(head_label)

        # Draw arrow from HEAD to first node
        draw_arrow(
            self.scene,
            self.start_x +self.node_width/2, self.start_y -25,
            self.start_x + self.node_width / 2, self.start_y,
            soft_yellow, 2
        )

        x = self.start_x
        y = self.start_y
        self.x_offset=0
        node = self.head
        order = []

        # Draw nodes
        while node:
            # Draw node rectangle (divided into value | next)
            rect = QGraphicsRectItem(x, y, self.node_width, self.node_height)
            rect.setBrush(soft_blue)
            rect.setPen(QPen(Qt.white, 2))
            self.scene.addItem(rect)

            # Draw divider line between value and next pointer
            divider = QGraphicsLineItem(
                x -10+ self.node_width * 0.6, y,
                x -10+ self.node_width * 0.6, y + self.node_height
            )
            divider.setPen(QPen(Qt.white, 1))
            self.scene.addItem(divider)

            # Draw value text
            text = QGraphicsSimpleTextItem(str(node.value))
            text.setBrush(Qt.white)
            font = QFont("Arial", 12, QFont.Bold)
            text.setFont(font)
            # Center the text in the value section
            text_rect = text.boundingRect()
            text_x = x + (self.node_width * 0.6 - text_rect.width()) / 2
            text_y = y + (self.node_height - text_rect.height()) / 2
            text.setPos(text_x, text_y)
            self.scene.addItem(text)

            #address
            addr_text = QGraphicsSimpleTextItem(str(node.address))
            addr_text.setBrush(Qt.white)
            addr_text.setPos(x +self.x_offset+28, y + 53)
            self.scene.addItem(addr_text)

            # Draw null indicator or arrow start point
            null_indicator = None
            if node.next is None:
                # Draw "NULL" or "X" in the next section
                null_text = QGraphicsSimpleTextItem("NULL")
                null_text.setBrush(soft_red)
                null_font = QFont("Arial", 9, QFont.Bold)
                null_text.setFont(null_font)
                null_rect = null_text.boundingRect()
                null_x = x-3 + self.node_width * 0.6 + (self.node_width * 0.4 - null_rect.width()) / 2
                null_y = y + (self.node_height - null_rect.height()) / 2
                null_text.setPos(null_x, null_y)
                self.scene.addItem(null_text)
                null_indicator = null_text

            self.graphics_nodes[node] = {
                'rect': rect,
                'text': text,
                'null_indicator': null_indicator
            }
            order.append(node)

            x += self.node_width + self.gap
            node = node.next

        #Draws the arrow beteen two nodes
        for node in order:
            if node.next:
                print("Drawing arrow called")
                print(node)

                rect = self.graphics_nodes[node]['rect']
                next_rect_item = self.graphics_nodes[node.next]['rect']

                # Position of the start of the arrow
                x1 = rect.x() + self.node_width+32+self.x_offset
                y1 = rect.y() + self.node_height / 2+80

                # Position at the end of the arrrow
                x2 = next_rect_item.x() + 160+self.x_offset
                y2 = next_rect_item.y() + self.node_height / 2+80

                draw_arrow(self.scene, x1, y1, x2, y2, Qt.white, 2) #calls the draw arrow function for head

                next_text = QGraphicsSimpleTextItem(str(node.next.address), rect)
                next_text.setBrush(Qt.white if node.next else soft_red)
                next_text.setFont(QFont("Arial", 9))
                next_rect = next_text.boundingRect()
                local_x = self.node_width * 0.6 + \
                                 (self.node_width * 0.4 - next_rect.width()) / 2
                local_y = (self.node_height - next_rect.height()) / 2

                next_text.setPos(local_x+self.x_offset +25, local_y+77)

                #Tail
                tail_label = QGraphicsSimpleTextItem("TAIL")
                tail_label.setBrush(soft_yellow)
                font = QFont("Arial", 10, QFont.Bold)
                tail_label.setFont(font)
                tail_label.setPos(self.end_x-70+self.offset_end+self.node_width/2, self.end_y - 40)
                self.scene.addItem(tail_label)

                # Draw arrow from HEAD to first node
                draw_arrow(
                    self.scene,
                    self.end_x-55+self.node_width/2 +self.offset_end, self.end_y-25,
                    self.end_x-55+ self.node_width / 2+ self.offset_end, self.end_y-2,
                    soft_yellow, 2
                )



            self.x_offset += 130 #offset the arrow to new position when a new node is added
        self.offset_end += 130
        # Adjust scene rect
        self.scene.setSceneRect(self.scene.itemsBoundingRect().adjusted(-20, -20, 20, 20))


    def draw_list_tail(self):
        self.scene.clear()
        self.graphics_nodes.clear()


        print("TAIL")
        tail_label = QGraphicsSimpleTextItem("TAIL")
        tail_label.setBrush(soft_yellow)
        font = QFont("Arial", 10, QFont.Bold)
        tail_label.setFont(font)
        tail_label.setPos(self.end_x-70+self.offset_end+self.node_width/2, self.end_y - 40)
        self.scene.addItem(tail_label)

        # Draw arrow from HEAD to first node
        draw_arrow(
            self.scene,
            self.end_x-55+self.node_width/2 +self.offset_end, self.end_y-25,
            self.end_x-55+ self.node_width / 2+ self.offset_end, self.end_y-2,
            soft_yellow, 2
        )

        x = self.start_x
        y = self.start_y
        self.x_offset=0
        node = self.head
        order = []

        # Draw nodes
        while node:
            # Draw node rectangle (divided into value | next)
            rect = QGraphicsRectItem(x, y, self.node_width, self.node_height)
            rect.setBrush(soft_blue)
            rect.setPen(QPen(Qt.white, 2))
            self.scene.addItem(rect)

            # Draw divider line between value and next pointer
            divider = QGraphicsLineItem(
                x -10+ self.node_width * 0.6, y,
                x -10+ self.node_width * 0.6, y + self.node_height
            )
            divider.setPen(QPen(Qt.white, 1))
            self.scene.addItem(divider)

            # Draw value text
            text = QGraphicsSimpleTextItem(str(node.value))
            text.setBrush(Qt.white)
            font = QFont("Arial", 12, QFont.Bold)
            text.setFont(font)
            # Center the text in the value section
            text_rect = text.boundingRect()
            text_x = x + (self.node_width * 0.6 - text_rect.width()) / 2
            text_y = y + (self.node_height - text_rect.height()) / 2
            text.setPos(text_x, text_y)
            self.scene.addItem(text)

            #address
            addr_text = QGraphicsSimpleTextItem(str(node.address))
            addr_text.setBrush(Qt.white)
            addr_text.setPos(x +self.x_offset+28, y + 53)
            self.scene.addItem(addr_text)

            # Draw null indicator or arrow start point
            null_indicator = None
            if node.next is None:
                # Draw "NULL" or "X" in the next section
                null_text = QGraphicsSimpleTextItem("NULL")
                null_text.setBrush(soft_red)
                null_font = QFont("Arial", 9, QFont.Bold)
                null_text.setFont(null_font)
                null_rect = null_text.boundingRect()
                null_x = x-3 + self.node_width * 0.6 + (self.node_width * 0.4 - null_rect.width()) / 2
                null_y = y + (self.node_height - null_rect.height()) / 2
                null_text.setPos(null_x, null_y)
                self.scene.addItem(null_text)
                null_indicator = null_text

            self.graphics_nodes[node] = {
                'rect': rect,
                'text': text,
                'null_indicator': null_indicator
            }
            order.append(node)

            x += self.node_width + self.gap
            node = node.next

        #Draws the arrow beteen two nodes
        for node in order:
            if node.next:
                print("Drawing arrow called")
                print(node)

                rect = self.graphics_nodes[node]['rect']
                next_rect_item = self.graphics_nodes[node.next]['rect']

                # Position of the start of the arrow
                x1 = rect.x() + self.node_width+32+self.x_offset
                y1 = rect.y() + self.node_height / 2+80

                # Position at the end of the arrrow
                x2 = next_rect_item.x() + 160+self.x_offset
                y2 = next_rect_item.y() + self.node_height / 2+80

                draw_arrow(self.scene, x1, y1, x2, y2, Qt.white, 2) #calls the draw arrow function for head

                next_text = QGraphicsSimpleTextItem(str(node.next.address), rect)
                next_text.setBrush(Qt.white if node.next else soft_red)
                next_text.setFont(QFont("Arial", 9))
                next_rect = next_text.boundingRect()
                local_x = self.node_width * 0.6 + \
                                 (self.node_width * 0.4 - next_rect.width()) / 2
                local_y = (self.node_height - next_rect.height()) / 2

                next_text.setPos(local_x+self.x_offset +25, local_y+77)

                #Head label after tail a node:
                head_label = QGraphicsSimpleTextItem("HEAD")
                head_label.setBrush(soft_yellow)
                font = QFont("Arial", 10, QFont.Bold)
                head_label.setFont(font)
                head_label.setPos(self.start_x-20+self.node_width/2, self.start_y - 40)
                self.scene.addItem(head_label)

                # Draw arrow from HEAD to first node
                draw_arrow(
                    self.scene,
                    self.start_x +self.node_width/2, self.start_y -25,
                    self.start_x + self.node_width / 2, self.start_y,
                    soft_yellow, 2
                )


            self.x_offset += 130 #offset the arrow to new position when a new node is added
        self.offset_end += 130

        # Adjust scene rect
        self.scene.setSceneRect(self.scene.itemsBoundingRect().adjusted(-20, -20, 20, 20))





       # Animation
    def animate_steps(self, steps, speed=500):
        self.steps = steps
        self.step_index = 0
        self.animation_speed = speed
        self.timer.stop()
        self.timer.start(self.animation_speed)

    def next_step(self):
        if self.step_index >= len(self.steps):
            self.timer.stop()

            return

        step = self.steps[self.step_index]
        action = step[0]

        # Reset all node colors
        for node_graphics in self.graphics_nodes.values():
                node_graphics['rect'].setBrush(soft_blue)

        if action == "visit":
            node = step[1]
            message = step[2] if len(step) > 2 else "Visiting node"
            self.highlight(node, soft_yellow)

        elif action == "compare":
            node, target = step[1], step[2]
            self.highlight(node, soft_orange)

        elif action == "insertHead":
            node,value = step[1], step[2]
            new_node = ListNode(value)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node

            self.draw_list_head()
            self.highlight(new_node, soft_green)

        elif action == "deleteHead":
            node, prev = step[1], step[2]
            self.highlight(node, soft_red)



        elif action == "removeHead":
            node, prev = step[1], step[2]

            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.clear()
            else:
                self.head = node.next

                self.draw_list_head_remove()


        elif action == "insertTail":
            value = step[1]
            new_node = ListNode(value)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

            self.draw_list_tail()
            self.highlight(new_node, soft_green)

        elif action == "deleteTail":
            node = step[1]
            self.highlight(node, soft_red)



        elif action == "removeTail":
            if self.head is None:
                return

            if self.head.next is None:
                # Only one node
                self.head = None
                self.tail = None
                self.clear()
                print("remove tail called")
                return
            else:
                curr = self.head
                while curr.next != self.tail:
                    curr = curr.next

                curr.next = None
                self.tail = curr

                self.draw_list_tail_remove()

        self.step_index += 1


    def highlight(self, node, color):
        if node not in self.graphics_nodes:
            return
        self.graphics_nodes[node]['rect'].setBrush(color)


    def clear(self):
        self.timer.stop()
        self.scene.clear()
        self.graphics_nodes.clear()
        self.head = None
        self.steps = []
        self.step_index = 0
        self.offset_end = 0
        self.x_offset = 0



    def draw_list_tail_remove(self):
        self.scene.clear()
        self.graphics_nodes.clear()


        print("TAIL")
        tail_label = QGraphicsSimpleTextItem("TAIL")
        tail_label.setBrush(soft_yellow)
        font = QFont("Arial", 10, QFont.Bold)
        tail_label.setFont(font)
        tail_label.setPos(self.end_x-70-260+self.offset_end+self.node_width/2, self.end_y - 40)
        self.scene.addItem(tail_label)

        # Draw arrow from HEAD to first node
        draw_arrow(
            self.scene,
            self.end_x-55+self.node_width/2 +self.offset_end-260, self.end_y-25,
            self.end_x-55+ self.node_width / 2+ self.offset_end-260, self.end_y-2,
            soft_yellow, 2
        )

        x = self.start_x
        y = self.start_y
        self.x_offset=0
        node = self.head
        order = []

        # Draw nodes
        while node:
            # Draw node rectangle (divided into value | next)
            rect = QGraphicsRectItem(x, y, self.node_width, self.node_height)
            rect.setBrush(soft_blue)
            rect.setPen(QPen(Qt.white, 2))
            self.scene.addItem(rect)

            # Draw divider line between value and next pointer
            divider = QGraphicsLineItem(
                x -10+ self.node_width * 0.6, y,
                x -10+ self.node_width * 0.6, y + self.node_height
            )
            divider.setPen(QPen(Qt.white, 1))
            self.scene.addItem(divider)

            # Draw value text
            text = QGraphicsSimpleTextItem(str(node.value))
            text.setBrush(Qt.white)
            font = QFont("Arial", 12, QFont.Bold)
            text.setFont(font)
            # Center the text in the value section
            text_rect = text.boundingRect()
            text_x = x + (self.node_width * 0.6 - text_rect.width()) / 2
            text_y = y + (self.node_height - text_rect.height()) / 2
            text.setPos(text_x, text_y)
            self.scene.addItem(text)

            #address
            addr_text = QGraphicsSimpleTextItem(str(node.address))
            addr_text.setBrush(Qt.white)
            addr_text.setPos(x +self.x_offset+28, y + 53)
            self.scene.addItem(addr_text)

            # Draw null indicator or arrow start point
            null_indicator = None
            if node.next is None:
                # Draw "NULL" or "X" in the next section
                null_text = QGraphicsSimpleTextItem("NULL")
                null_text.setBrush(soft_red)
                null_font = QFont("Arial", 9, QFont.Bold)
                null_text.setFont(null_font)
                null_rect = null_text.boundingRect()
                null_x = x-3 + self.node_width * 0.6 + (self.node_width * 0.4 - null_rect.width()) / 2
                null_y = y + (self.node_height - null_rect.height()) / 2
                null_text.setPos(null_x, null_y)
                self.scene.addItem(null_text)
                null_indicator = null_text

            self.graphics_nodes[node] = {
                'rect': rect,
                'text': text,
                'null_indicator': null_indicator
            }
            order.append(node)

            x += self.node_width + self.gap
            node = node.next

        #Draws the arrow beteen two nodes
        for node in order:
            if node.next:
                print("Drawing arrow called")
                print(node)

                rect = self.graphics_nodes[node]['rect']
                next_rect_item = self.graphics_nodes[node.next]['rect']

                # Position of the start of the arrow
                x1 = rect.x() + self.node_width+32+self.x_offset
                y1 = rect.y() + self.node_height / 2+80

                # Position at the end of the arrrow
                x2 = next_rect_item.x() + 160+self.x_offset
                y2 = next_rect_item.y() + self.node_height / 2+80

                draw_arrow(self.scene, x1, y1, x2, y2, Qt.white, 2) #calls the draw arrow function for head

                next_text = QGraphicsSimpleTextItem(str(node.next.address), rect)
                next_text.setBrush(Qt.white if node.next else soft_red)
                next_text.setFont(QFont("Arial", 9))
                next_rect = next_text.boundingRect()
                local_x = self.node_width * 0.6 + \
                                 (self.node_width * 0.4 - next_rect.width()) / 2
                local_y = (self.node_height - next_rect.height()) / 2

                next_text.setPos(local_x+self.x_offset +25, local_y+77)

                #Head label after tail a node:
                head_label = QGraphicsSimpleTextItem("HEAD")
                head_label.setBrush(soft_yellow)
                font = QFont("Arial", 10, QFont.Bold)
                head_label.setFont(font)
                head_label.setPos(self.start_x-20+self.node_width/2, self.start_y - 40)
                self.scene.addItem(head_label)

                # Draw arrow from HEAD to first node
                draw_arrow(
                    self.scene,
                    self.start_x +self.node_width/2, self.start_y -25,
                    self.start_x + self.node_width / 2, self.start_y,
                    soft_yellow, 2
                )


            self.x_offset += 130 #offset the arrow to new position when a new node is added
        self.offset_end -= 130

        # Adjust scene rect
        self.scene.setSceneRect(self.scene.itemsBoundingRect().adjusted(-20, -20, 20, 20))



    def draw_list_head_remove(self):
        self.scene.clear()
        self.graphics_nodes.clear()


        print("TAIL")
        tail_label = QGraphicsSimpleTextItem("TAIL")
        tail_label.setBrush(soft_yellow)
        font = QFont("Arial", 10, QFont.Bold)
        tail_label.setFont(font)
        tail_label.setPos(self.end_x-70-260+self.offset_end+self.node_width/2, self.end_y - 40)
        self.scene.addItem(tail_label)

        # Draw arrow from HEAD to first node
        draw_arrow(
            self.scene,
            self.end_x-55+self.node_width/2 +self.offset_end-260, self.end_y-25,
            self.end_x-55+ self.node_width / 2+ self.offset_end-260, self.end_y-2,
            soft_yellow, 2
        )

        x = self.start_x
        y = self.start_y
        self.x_offset=0
        node = self.head
        order = []

        # Draw nodes
        while node:
            # Draw node rectangle (divided into value | next)
            rect = QGraphicsRectItem(x, y, self.node_width, self.node_height)
            rect.setBrush(soft_blue)
            rect.setPen(QPen(Qt.white, 2))
            self.scene.addItem(rect)

            # Draw divider line between value and next pointer
            divider = QGraphicsLineItem(
                x -10+ self.node_width * 0.6, y,
                x -10+ self.node_width * 0.6, y + self.node_height
            )
            divider.setPen(QPen(Qt.white, 1))
            self.scene.addItem(divider)

            # Draw value text
            text = QGraphicsSimpleTextItem(str(node.value))
            text.setBrush(Qt.white)
            font = QFont("Arial", 12, QFont.Bold)
            text.setFont(font)
            # Center the text in the value section
            text_rect = text.boundingRect()
            text_x = x + (self.node_width * 0.6 - text_rect.width()) / 2
            text_y = y + (self.node_height - text_rect.height()) / 2
            text.setPos(text_x, text_y)
            self.scene.addItem(text)

            #address
            addr_text = QGraphicsSimpleTextItem(str(node.address))
            addr_text.setBrush(Qt.white)
            addr_text.setPos(x +self.x_offset+28, y + 53)
            self.scene.addItem(addr_text)

            # Draw null indicator or arrow start point
            null_indicator = None
            if node.next is None:
                # Draw "NULL" or "X" in the next section
                null_text = QGraphicsSimpleTextItem("NULL")
                null_text.setBrush(soft_red)
                null_font = QFont("Arial", 9, QFont.Bold)
                null_text.setFont(null_font)
                null_rect = null_text.boundingRect()
                null_x = x-3 + self.node_width * 0.6 + (self.node_width * 0.4 - null_rect.width()) / 2
                null_y = y + (self.node_height - null_rect.height()) / 2
                null_text.setPos(null_x, null_y)
                self.scene.addItem(null_text)
                null_indicator = null_text

            self.graphics_nodes[node] = {
                'rect': rect,
                'text': text,
                'null_indicator': null_indicator
            }
            order.append(node)

            x += self.node_width + self.gap
            node = node.next

        #Draws the arrow beteen two nodes
        for node in order:
            if node.next:
                print("Drawing arrow called")
                print(node)

                rect = self.graphics_nodes[node]['rect']
                next_rect_item = self.graphics_nodes[node.next]['rect']

                # Position of the start of the arrow
                x1 = rect.x() + self.node_width+32+self.x_offset
                y1 = rect.y() + self.node_height / 2+80

                # Position at the end of the arrrow
                x2 = next_rect_item.x() + 160+self.x_offset
                y2 = next_rect_item.y() + self.node_height / 2+80

                draw_arrow(self.scene, x1, y1, x2, y2, Qt.white, 2) #calls the draw arrow function for head

                next_text = QGraphicsSimpleTextItem(str(node.next.address), rect)
                next_text.setBrush(Qt.white if node.next else soft_red)
                next_text.setFont(QFont("Arial", 9))
                next_rect = next_text.boundingRect()
                local_x = self.node_width * 0.6 + \
                                 (self.node_width * 0.4 - next_rect.width()) / 2
                local_y = (self.node_height - next_rect.height()) / 2

                next_text.setPos(local_x+self.x_offset +25, local_y+77)

                #Head label after tail a node:
                head_label = QGraphicsSimpleTextItem("HEAD")
                head_label.setBrush(soft_yellow)
                font = QFont("Arial", 10, QFont.Bold)
                head_label.setFont(font)
                head_label.setPos(self.start_x-20+self.node_width/2, self.start_y - 40)
                self.scene.addItem(head_label)

                # Draw arrow from HEAD to first node
                draw_arrow(
                    self.scene,
                    self.start_x +self.node_width/2, self.start_y -25,
                    self.start_x + self.node_width / 2, self.start_y,
                    soft_yellow, 2
                )


            self.x_offset += 130 #offset the arrow to new position when a new node is added
        self.offset_end -= 130

        # Adjust scene rect
        self.scene.setSceneRect(self.scene.itemsBoundingRect().adjusted(-20, -20, 20, 20))







