#include "arraywindow.h"
#include "ui_arraywindow.h"

Arraywindow::Arraywindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Arraywindow)
{
    ui->setupUi(this);
}

Arraywindow::~Arraywindow()
{
    delete ui;
}
