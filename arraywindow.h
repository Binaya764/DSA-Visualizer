#ifndef ARRAYWINDOW_H
#define ARRAYWINDOW_H

#include <QMainWindow>

namespace Ui {
class Arraywindow;
}

class Arraywindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit Arraywindow(QWidget *parent = nullptr);
    ~Arraywindow();

private:
    Ui::Arraywindow *ui;
};

#endif // ARRAYWINDOW_H
