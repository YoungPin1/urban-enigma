import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.run()
        self.init_table()

    def init_table(self):
        self.tbl_wdt.setHorizontalHeaderLabels(['Название сорта', 'Степень обжарки', 'Молотый/В Зернах',
                                                'Описание вкуса', 'Цена в рублях', 'Объем в граммах'])
        head_view = self.tbl_wdt.horizontalHeader()
        head_view.setSectionResizeMode(0, 3)
        head_view.setSectionResizeMode(1, 3)
        head_view.setSectionResizeMode(2, 3)
        head_view.setSectionResizeMode(3, 3)
        head_view.setSectionResizeMode(4, 3)
        head_view.setSectionResizeMode(5, 3)
        self.tbl_wdt.resizeColumnsToContents()

    def run(self):
        self.fill_table(self.load_db())

    def load_db(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        return cur.execute("""SELECT name, roast, type, description, price, volume FROM data""").fetchall()

    def fill_table(self, types):
        self.tbl_wdt.setColumnCount(6)
        self.tbl_wdt.setRowCount(len(types))
        for i in range(len(types)):
            for j in range(6):
                self.tbl_wdt.setItem(i, j, QTableWidgetItem(str(types[i][j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
