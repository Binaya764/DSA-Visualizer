#include "visualizer.h"
#include <QBrush>

Visualizer::Visualizer(QWidget *parent)
    : QGraphicsView(parent), scene(new QGraphicsScene(this)) {
    setScene(scene);
}

void Visualizer::drawArray(const QVector<int> &arr) {
    scene->clear();
    bars.clear();

    int barWidth = width() / arr.size();
    for(int i = 0; i < arr.size(); i++) {
        int height = arr[i] * 3;  // scale
        QGraphicsRectItem *bar = scene->addRect(i * barWidth, 400 - height, barWidth - 2, height, Qt::NoPen, Qt::blue);
        bars.append(bar);
    }
}

void Visualizer::highlightBars(int i, int j, QColor color) {
    if(i >= 0 && i < bars.size()) bars[i]->setBrush(color);
    if(j >= 0 && j < bars.size()) bars[j]->setBrush(color);
}
