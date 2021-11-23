import sqlite3

from PyQt5.QtWidgets import QMainWindow

import main
from addEditCoffeeForm import Ui_MainWindow


class AddEdit(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.run()
        main.Coffee.fill_table(self.tbl_wdt, main.Coffee.load_db())
        main.Coffee.init_table(self.tbl_wdt)

    def run(self):
        self.btn_add.clicked.connect(self.add_row)
        self.btn_del.clicked.connect(self.del_row)
        self.btn_save.clicked.connect(self.save_table)

    def add_row(self):
        row_count = self.tbl_wdt.rowCount()
        self.tbl_wdt.insertRow(row_count)

    def del_row(self):
        if self.ledit_del.text() != '':
            self.tbl_wdt.removeRow(int((self.ledit_del.text())) - 1)

    def save_table(self):
        all_words = []
        for i in range(self.tbl_wdt.rowCount()):
            row = []
            for j in range(self.tbl_wdt.columnCount()):
                item = self.tbl_wdt.item(i, j)
                if item is not None:
                    row.append(str(item.text()))
                else:
                    row.append('')
            all_words.append(row)
        self.save_db(all_words)

    def save_db(self, all_words):
        con = sqlite3.connect('C:/Users/Batta/Desktop/Lesson 12. Git repo/data/coffee.sqlite')
        cur = con.cursor()
        cur.execute('DELETE FROM data')
        for row in all_words:
            cur.execute("""INSERT INTO data (name, roast, type, description, price, volume) 
            VALUES(?, ?, ?, ?, ?, ?)""", (row[0], row[1], row[2], row[3], row[4], row[5]))
            con.commit()
        self.back_to_main()

    def back_to_main(self):
        self.main_window = main.Coffee()
        self.hide()
        self.main_window.show()

# def except_hook(cls, exception, traceback):
#     sys.__excepthook__(cls, exception, traceback)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = AddEdit()
#     ex.show()
#     sys.excepthook = except_hook
#     sys.exit(app.exec())
