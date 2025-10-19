#ifndef SORTING_ALGORITHM_H
#define SORTING_ALGORITHM_H

#include <QObject>
#include <QVector>

class SortingAlgorithms : public QObject
{
    Q_OBJECT   // 👈 Must be inside class

public:
    explicit SortingAlgorithms(QObject *parent = nullptr);

signals:
    void swapOccurred(int i, int j);
    void compareOccurred(int i, int j);

public slots:
    void bubbleSort(QVector<int> &arr);
    void selectionSort(QVector<int> &arr);
    void insertionSort(QVector<int> &arr);
};

#endif // SORTING_ALGORITHM_H
