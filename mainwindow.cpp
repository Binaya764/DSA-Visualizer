#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QRandomGenerator>
#include <QBrush>
#include <QColor>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    scene = new QGraphicsScene(this);
    ui->graphicsView->setScene(scene);

    timer = new QTimer(this);
    connect(timer, &QTimer::timeout, this, &MainWindow::bubbleSortStep);

    connect(ui->Generate_array, &QPushButton::clicked, this, &MainWindow::generateArray);
    connect(ui->Sort_button, &QPushButton::clicked, this, &MainWindow::startSorting);

    // Initialize slider speed
    ui->horizontalSlider->setMinimum(1);
    ui->horizontalSlider->setMaximum(200);
    ui->horizontalSlider->setValue(50);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::generateArray() {
    array.clear();
    bars.clear();
    scene->clear();

    int n = 30;
    for (int i = 0; i < n; i++)
        array.append(QRandomGenerator::global()->bounded(10, 100));

    drawArray();
    i = j = 0;
}

void MainWindow::drawArray() {
    scene->clear();
    bars.clear();

    int width = ui->graphicsView->width();
    int barWidth = width / array.size();

    for (int k = 0; k < array.size(); k++) {
        int height = array[k] * 3;
        auto *bar = scene->addRect(k * barWidth, 300 - height, barWidth - 2, height, Qt::NoPen, QBrush(Qt::blue));
        bars.append(bar);
    }
}

void MainWindow::swapBars(int a, int b) {
    qSwap(array[a], array[b]);
    drawArray();
    bars[a]->setBrush(Qt::red);
    bars[b]->setBrush(Qt::red);
}

void MainWindow::startSorting() {
    delay = 201 - ui->horizontalSlider->value(); // lower slider = slower
    i = j = 0;
    timer->start(delay);
}

void MainWindow::bubbleSortStep() {
    if (i < array.size() - 1) {
        if (j < array.size() - i - 1) {
            if (array[j] > array[j + 1]) {
                swapBars(j, j + 1);
            }
            j++;
        } else {
            j = 0;
            i++;
        }
    } else {
        timer->stop();
    }
}
