#include "sorting_algorithm.h"
#include <QThread>

SortingAlgorithms::SortingAlgorithms(QObject *parent)
    : QObject(parent)
{
}

void SortingAlgorithms::bubbleSort(QVector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            emit compareOccurred(j, j + 1);
            if (arr[j] > arr[j + 1]) {
                qSwap(arr[j], arr[j + 1]);
                emit swapOccurred(j, j + 1);
            }
            QThread::msleep(100);
        }
    }
}

void SortingAlgorithms::selectionSort(QVector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < n; ++j) {
            emit compareOccurred(minIndex, j);
            if (arr[j] < arr[minIndex])
                minIndex = j;
        }
        if (minIndex != i) {
            qSwap(arr[i], arr[minIndex]);
            emit swapOccurred(i, minIndex);
        }
        QThread::msleep(100);
    }
}

void SortingAlgorithms::insertionSort(QVector<int> &arr)
{
    int n = arr.size();
    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            emit swapOccurred(j, j + 1);
            j--;
            QThread::msleep(100);
        }
        arr[j + 1] = key;
    }
}
