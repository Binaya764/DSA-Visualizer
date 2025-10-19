#ifndef VISUALIZER_H
#define VISUALIZER_H

#include <QGraphicsView>
#include <QGraphicsRectItem>
#include <QVector>

class Visualizer : public QGraphicsView {
    Q_OBJECT
public:
    explicit Visualizer(QWidget *parent = nullptr);
    void drawArray(const QVector<int> &arr);
    void highlightBars(int i, int j, QColor color);

private:
    QGraphicsScene *scene;
    QVector<QGraphicsRectItem*> bars;
};

#endif // VISUALIZER_H
