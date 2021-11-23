import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView

import add_edit
from main_design import Ui_MainWindow


class Coffee(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.run()
        self.fill_table(self.tbl_wdt, self.load_db())
        self.init_table(self.tbl_wdt)
        self.tbl_wdt.setEditTriggers(QAbstractItemView.NoEditTriggers)

    @staticmethod
    def init_table(table):
        table.setHorizontalHeaderLabels(['Название сорта', 'Степень обжарки', 'Молотый/В Зернах',
                                         'Описание вкуса', 'Цена в рублях', 'Объем в граммах'])
        head_view = table.horizontalHeader()
        head_view.setSectionResizeMode(0, 3)
        head_view.setSectionResizeMode(1, 3)
        head_view.setSectionResizeMode(2, 3)
        head_view.setSectionResizeMode(3, 3)
        head_view.setSectionResizeMode(4, 3)
        head_view.setSectionResizeMode(5, 3)
        table.resizeColumnsToContents()

    def run(self):
        self.btn_edit.clicked.connect(self.edit)

    @staticmethod
    def load_db():
        con = sqlite3.connect('C:/Users/Batta/Desktop/Lesson 12. Git repo/data/coffee.sqlite')
        cur = con.cursor()
        return cur.execute("""SELECT name, roast, type, description, price, volume FROM data""").fetchall()

    @staticmethod
    def fill_table(table, types):
        table.setColumnCount(6)
        table.setRowCount(len(types))
        for i in range(len(types)):
            for j in range(6):
                table.setItem(i, j, QTableWidgetItem(str(types[i][j])))

    def edit(self):
        self.edit_window = add_edit.AddEdit()
        self.hide()
        self.edit_window.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
